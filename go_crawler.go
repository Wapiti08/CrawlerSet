package main

import (
	"fmt"
	http "net/http"
	"os"
	"strings"

	html "golang.org/x/net/html"
)

func getHref(t html.Token) (ok bool, href string) {
	for _, a := range t.Attr {
		if a.Key == "href" {
			href = a.Val
			ok = true
		}
	}
	return
}

// crawl with channel
func crawl(url string, ch chan string, chFinished chan bool) {
	/*
		param url: the url to crawl for information
		param ch: the channel to save extracted shared urls
		param chFinished: the channel to save status
	*/
	// publish the urls if finds to shared channel
	resp, err := http.Get(url)

	defer func() {
		chFinished <- true
	}()

	if err != nil {
		return
	}

	b := resp.Body
	defer b.Close()

	// parse the response
	z := html.NewTokenizer(b)

	for {
		tt := z.Next()
		// switch used with concrete types
		switch {
		case tt == html.ErrorToken:
			return
		case tt == html.StartTagToken:
			t := z.Token()

			isAnchor := t.Data == "a"
			if !isAnchor {
				continue
			}

			ok, url := getHref(t)
			if !ok {
				continue
			}

			// make sure the url begins with http**
			hasProto := strings.Index(url, "http") == 0
			if hasProto {
				// second channel for communication status
				ch <- url
			}
		}
	}

}

// example of cocurrency

func main() {
	foundUrls := make(map[string]bool)
	seedUrls := os.Args[1:]

	// Channels
	chUrls := make(chan string)
	chFinished := make(chan bool)

	// multiple crawl process
	for _, url := range seedUrls {
		// cocurrecy scraping
		go crawl(url, chUrls, chFinished)
	}
	// subscribe to both channels
	for c := 0; c < len(seedUrls); {
		// select is used with channels
		select {
		case url := <-chUrls:
			foundUrls[url] = true
		case <-chFinished:
			// increase c if there is one url finished
			c++
		}
	}
	// print out the results
	fmt.Println("\nFound", len(foundUrls), "unique urls: \n")

	for url, _ := range foundUrls {
		fmt.Println(" - " + url)
	}

	close(chUrls)
	close(chFinished)
}
