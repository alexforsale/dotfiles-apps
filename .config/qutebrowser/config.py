#!/usr/bin/env python
"""Qtile configuration."""
import subprocess


# pylint: disable=C0111
c = c  # noqa: F821 pylint: disable=E0602,C0103
config = config  # noqa: F821 pylint: disable=E0602,C0103


def read_xresources(prefix):
    """Read settings from xresources."""
    props = {}
    x = subprocess.run(["xrdb", "-query"], stdout=subprocess.PIPE)
    lines = x.stdout.decode().split("\n")
    for line in filter(lambda l: l.startswith(prefix), lines):
        prop, _, value = line.partition(":\t")
        props[prop] = value
    return props


xresources = read_xresources("*")

c.colors.completion.category.bg = 'qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0 xresources["*.background"], stop:1 xresources["*.color13"])'
c.colors.completion.category.border.bottom = xresources["*.background"]
c.colors.completion.category.border.top = xresources["*.background"]
c.colors.completion.category.fg = xresources["*.foreground"]
c.colors.completion.fg = [
    xresources["*.foreground"],
    xresources["*.foreground"],
    xresources["*.foreground"],
]
c.colors.completion.item.selected.bg = xresources["*.background"]
c.colors.completion.item.selected.border.top = xresources["*.color11"]
c.colors.completion.item.selected.fg = xresources["*.color15"]
c.colors.completion.item.selected.match.fg = xresources["*.color1"]
c.colors.completion.match.fg = xresources["*.color15"]
c.colors.completion.even.bg = xresources["*.background"]
c.colors.completion.odd.bg = xresources["*.background"]
c.colors.completion.scrollbar.bg = xresources["*.background"]
c.colors.completion.scrollbar.fg = xresources["*.color15"]
c.colors.contextmenu.disabled.bg = xresources["*.background"]
c.colors.contextmenu.disabled.fg = xresources["*.foreground"]
c.colors.contextmenu.menu.bg = xresources["*.background"]
c.colors.contextmenu.menu.fg = xresources["*.foreground"]
c.colors.contextmenu.selected.bg = xresources["*.background"]
c.colors.contextmenu.selected.fg = xresources["*.foreground"]
c.colors.downloads.bar.bg = xresources["*.background"]
c.colors.downloads.error.bg = xresources["*.color9"]
c.colors.downloads.error.fg = xresources["*.foreground"]
c.colors.downloads.start.bg = xresources["*.color12"]
c.colors.downloads.start.fg = xresources["*.foreground"]
c.colors.downloads.stop.bg = xresources["*.color14"]
c.colors.downloads.stop.fg = xresources["*.foreground"]
c.colors.downloads.system.bg = "rgb"
c.colors.downloads.system.fg = "rgb"
c.colors.hints.bg = "qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0 rgba(255, 247, 133, 0.8), stop:1 rgba(255, 197, 66, 0.8))"
c.colors.hints.fg = xresources["*.background"]
c.colors.hints.match.fg = xresources["*.color6"]
c.colors.keyhint.bg = "rgba(0, 0, 0, 80%)"
c.colors.keyhint.fg = xresources["*.color15"]
c.colors.keyhint.suffix.fg = xresources["*.color11"]
c.colors.messages.error.bg = xresources["*.color9"]
c.colors.messages.error.border = xresources["*.color9"]

c.colors.messages.info.bg = xresources["*.background"]
c.colors.messages.info.border = xresources["*.background"]
c.colors.messages.info.fg = xresources["*.foreground"]
c.colors.messages.warning.bg = "darkorange"
c.colors.messages.warning.border = xresources["*.color3"]
c.colors.messages.warning.fg = xresources["*.background"]
c.colors.prompts.bg = xresources["*.background"]
c.colors.prompts.border = "1px solid gray"
c.colors.prompts.fg = xresources["*.foreground"]
c.colors.prompts.selected.bg = "grey"
c.colors.statusbar.caret.bg = xresources["*.background"]
c.colors.statusbar.caret.fg = xresources["*.foreground"]
c.colors.statusbar.caret.selection.bg = xresources["*.background"]
c.colors.statusbar.caret.selection.fg = xresources["*.foreground"]
c.colors.statusbar.command.bg = xresources["*.background"]
c.colors.statusbar.command.fg = xresources["*.foreground"]
c.colors.statusbar.command.private.bg = xresources["*.background"]
c.colors.statusbar.command.private.fg = xresources["*.color15"]
c.colors.statusbar.insert.bg = "darkgreen"
c.colors.statusbar.insert.fg = xresources["*.foreground"]
c.colors.statusbar.normal.bg = xresources["*.background"]
c.colors.statusbar.normal.fg = xresources["*.foreground"]
c.colors.statusbar.passthrough.bg = xresources["*.background"]
c.colors.statusbar.passthrough.fg = xresources["*.foreground"]
c.colors.statusbar.private.bg = xresources["*.background"]
c.colors.statusbar.private.fg = xresources["*.color15"]
c.colors.statusbar.progress.bg = xresources["*.color13"]
c.colors.statusbar.url.error.fg = xresources["*.color14"]
c.colors.statusbar.url.fg = xresources["*.foreground"]
c.colors.statusbar.url.hover.fg = xresources["*.color14"]
c.colors.statusbar.url.success.http.fg = xresources["*.foreground"]
c.colors.statusbar.url.success.https.fg = xresources["*.color15"]
c.colors.statusbar.url.warn.fg = "yellow"
c.colors.tabs.bar.bg = xresources["*.color13"]
c.colors.tabs.even.bg = xresources["*.color13"]
c.colors.tabs.even.fg = xresources["*.foreground"]
c.colors.tabs.indicator.error = xresources["*.color10"]
c.colors.tabs.indicator.start = xresources["*.color12"]
c.colors.tabs.indicator.stop = xresources["*.color6"]
c.colors.tabs.indicator.system = "rgb"
c.colors.tabs.odd.bg = xresources["*.color13"]
c.colors.tabs.odd.fg = xresources["*.foreground"]
c.colors.tabs.pinned.even.bg = xresources["*.color13"]
c.colors.tabs.pinned.even.fg = xresources["*.foreground"]
c.colors.tabs.pinned.odd.bg = xresources["*.color13"]
c.colors.tabs.pinned.odd.fg = xresources["*.foreground"]
c.colors.tabs.pinned.selected.even.bg = xresources["*.color12"]
c.colors.tabs.pinned.selected.even.fg = xresources["*.color15"]
c.colors.tabs.pinned.selected.odd.bg = xresources["*.color11"]
c.colors.tabs.pinned.selected.odd.fg = xresources["*.color15"]
c.colors.tabs.selected.even.bg = xresources["*.color11"]
c.colors.tabs.selected.even.fg = xresources["*.color15"]
c.colors.tabs.selected.odd.bg = xresources["*.color11"]
c.colors.tabs.selected.odd.fg = xresources["*.color15"]
c.colors.webpage.bg = ""  # xresources['*.background']
c.colors.webpage.darkmode.algorithm = "lightness-cielab"
c.colors.webpage.darkmode.contrast = 0.0
c.colors.webpage.darkmode.enabled = True
c.colors.webpage.darkmode.grayscale.all = False
c.colors.webpage.darkmode.grayscale.images = 0.0
c.colors.webpage.darkmode.policy.images = "smart"
c.colors.webpage.darkmode.policy.page = "smart"
c.colors.webpage.darkmode.threshold.background = 0
c.colors.webpage.darkmode.threshold.text = 256
c.colors.webpage.preferred_color_scheme = "auto"

config.set(
    "content.headers.accept_language", "", "https://matchmaker.krunker.io/*"
)

config.set(
    "content.headers.user_agent",
    "Mozilla/5.0 ({os_info}) AppleWebKit/{webkit_version} (KHTML, like Gecko) {upstream_browser_key}/{upstream_browser_version} Safari/{webkit_version}",
    "https://web.whatsapp.com/",
)

config.set(
    "content.headers.user_agent",
    'content.headers.user_agent "Mozilla/5.0 ({os_info}; rv:90.0) Gecko/20100101 Firefox/90.0',
    "https://accounts.google.com/*",
)

config.set(
    "content.headers.user_agent",
    "Mozilla/5.0 ({os_info}) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99 Safari/537.36",
    "https://*.slack.com/*",
)

config.set("content.headers.accept_language", "en-US", "en;q=0.5")
c.content.headers.custom = {
    "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8"
}

c.url.searchengines = {
    "DEFAULT": "https://duckduckgo.com/?q={}",
    "goo": "https://google.com/search?q={}",
    "wa": "https://wiki.archlinux.org/?search={}",
    "ge": "https://wiki.gentoo.org/?search={}",
    "r/": "https://www.reddit.com/search/?q={}",
    "yt": "https://www.youtube.com/results?search_query={}",
}

config.set("content.images", True, "chrome-devtools://*")
config.set("content.images", True, "devtools://*")

c.zoom.default = "100%"

config.set("content.javascript.enabled", True, "chrome-devtools://*")
config.set("content.javascript.enabled", True, "devtools://*")
config.set("content.javascript.enabled", True, "chrome://*/*")
config.set("content.javascript.enabled", True, "qute://*/*")

config.load_autoconfig(False)

c.auto_save.session = True

config.set("content.cookies.accept", "all", "chrome-devtools://*")

config.bind(
    "Cr",
    "open javascript:location.href='org-protocol://roam-ref?template=r&ref='+encodeURIComponent(location.href)+'&title='+encodeURIComponent(document.title)",
)

config.bind(
    "Cl",
    "open javascript:location.href='org-protocol://capture?template=l&url='+encodeURIComponent(location.href)+'&title='+encodeURIComponent(document.title)",
)

config.bind("<ctrl-g>", "mode-leave", mode="insert")
config.bind("<ctrl-g>", "mode-leave", mode="prompt")
config.bind("<ctrl-g>", "mode-leave", mode="command")
config.bind("<ctrl-g>", "mode-leave", mode="hint")

config.bind("<ctrl-j>", "completion-item-focus next", mode="command")
config.bind("<ctrl-k>", "completion-item-focus prev", mode="command")

config.bind("<Down>", "completion-item-focus next", mode="command")
config.bind("<Up>", "completion-item-focus prev", mode="command")

config.unbind("<ctrl-p>")
config.unbind("<ctrl-n>")
config.bind("<ctrl-n>", "completion-item-focus next", mode="command")
config.bind("<ctrl-p>", "completion-item-focus prev", mode="command")

config.bind("<ctrl-p>", "prompt-item-focus prev", mode="prompt")
config.bind("<Up>", "prompt-item-focus prev", mode="prompt")
config.bind("<ctrl-n>", "prompt-item-focus next", mode="prompt")
config.bind("<Down>", "prompt-item-focus next", mode="prompt")
config.bind("y", "prompt-accept yes", mode="prompt")
config.bind("n", "prompt-accept no", mode="prompt")

config.unbind("<ctrl-a>")
config.bind("<Ctrl-n>", "scroll down")
config.bind("<Ctrl-p>", "scroll up")
config.bind("<Ctrl-a>", "back")
config.bind("<Ctrl-e>", "forward")

config.unbind("<ctrl-x>")
config.bind("<ctrl-x><ctrl-l>", "config-source")

config.bind("<Ctrl-x><Ctrl-f>", "set-cmd-text -s :open -t")
config.unbind("<ctrl-u>")
config.bind("<ctrl-u><Ctrl-x><Ctrl-f>", "set-cmd-text -s :open")

config.bind("<Ctrl-x><Ctrl-c>", "quit")

config.bind("<Alt-x>", "set-cmd-text :")

c.fonts.default_family = [
    "Source Code Pro",
    "Source Sans Pro",
    "Source Serif Pro",
    "Fantasque Sans Mono",
    "Liberation Mono",
    "Liberation Sans",
]
c.fonts.web.family.standard = "Source Code Pro"
c.fonts.web.family.fixed = "Source Code Pro"
c.fonts.web.family.fantasy = "Source Code Pro"
c.fonts.web.family.cursive = "Source Code Pro"
c.fonts.web.family.serif = "Source Serif Pro"
c.fonts.web.family.sans_serif = "Source Serif Pro"
c.fonts.contextmenu = "Source Code Pro"

# source wal colorscheme
config.source("qutewal.py")
