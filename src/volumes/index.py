# PAGE(Home)

from html_writer import HTMLWriter, HTMLMode;
from builder import Builder;

def build(env, self, html: HTMLWriter):
    builder = Builder(html);

    html.heading(1, "Volumes");
    html.newline();

    html.text("Booklet PDFs are intended for print and are not suitable for reading.");
    html.newline();

    builder.bank(self.parent);
