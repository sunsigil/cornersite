# PAGE(Home)

from html_writer import HTMLWriter, HTMLMode;

def build(env, self, html: HTMLWriter):
	html.heading(1, "Cornerlight Home Page");
	html.newline();

	html.text("For now, this is an internal site. Please do not share it with people outside of Cornerlight.");

	html.link("Interest Form", "https://docs.google.com/forms/d/e/1FAIpQLSeF3szRpMJT9puLkjm_bSyRpTZ3o3xtk9ZjpDnJlCY9T3g6NQ/viewform?usp=header");
	html.newline();
	html.link("Volumes", "volumes/index.html");
	html.newline();
	html.link("Itch", "https://sunsigil.itch.io/cornerlight");
