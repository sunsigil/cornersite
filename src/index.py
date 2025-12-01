#!/usr/bin/env python3

# PAGE(Home)

from html_writer import HTMLWriter, HTMLMode;

def build(here, html: HTMLWriter):
	html.heading(1, "Cornerlight Home Page");
	html.newline();

	html.link("Drive", "https://drive.google.com/drive/u/0/folders/1A6tQIlEG87xxfs52wX-tnvT1XVfzIZtP");
	html.newline();
	html.link("Interest Form", "https://docs.google.com/forms/d/e/1FAIpQLSeF3szRpMJT9puLkjm_bSyRpTZ3o3xtk9ZjpDnJlCY9T3g6NQ/viewform?usp=header");
	html.newline();
	html.link("Volumes", "volumes/index.html");
