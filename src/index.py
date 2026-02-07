# PAGE(Home)

from html_writer import HTMLWriter, HTMLMode;

def build(env, self, html: HTMLWriter):
	html.heading(1, "Cornerlight Home Page");
	html.newline();

	html.heading(2, "Announcements");
	html.text("For now, this is an internal site. Please do not share it with people outside of Cornerlight.");
	html.newline();
	html.text("We are currently working on Volume 6. The theme is \"New Year\".");
	html.newline();

	html.heading(2, "Links");
	html.link("Interest Form", "https://docs.google.com/forms/d/e/1FAIpQLSeF3szRpMJT9puLkjm_bSyRpTZ3o3xtk9ZjpDnJlCY9T3g6NQ/viewform?usp=header");
	html.newline();
	html.link("Submission Form", "https://docs.google.com/forms/d/e/1FAIpQLSeF3szRpMJT9puLkjm_bSyRpTZ3o3xtk9ZjpDnJlCY9T3g6NQ/viewform?usp=header");
	html.newline();
	html.link("Drive", "https://drive.google.com/drive/folders/1A6tQIlEG87xxfs52wX-tnvT1XVfzIZtP?usp=drive_link");
	html.newline();
	html.link("Itch", "https://sunsigil.itch.io/cornerlight");
	html.newline();

	html.heading(2, "FAQ");

	html.heading(3, "Can I contribute to the current Cornerlight issue?");
	html.text("No. It's already underway.");
	html.newline();

	html.heading(3, "Can I contribute to the next Cornerlight issue?");
	html.text("Yes! Please fill out the interest form linked above.");
	html.newline();

	html.heading(3, "How should I submit my pages?");
	html.text("Please upload them via the submission form linked above. One file per page is ideal.");
	html.newline();

	html.heading(3, "What file format is best for submissions?");
	html.text("Anything that is commonly accepted by software that normal people use. PDF is great, PNG is great, JPG is great. Nothing too weird please.");
	html.newline();
