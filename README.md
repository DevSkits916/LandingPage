# DevSkits Landing Page

A compact, standalone landing page for **Travis Ramsey / DevSkits**, with a matching HTML email signature.

The page uses a navy-and-blue theme, an animated SVG DevSkits intro, and a responsive layout. Contact information appears first, social links follow, and the GoFundMe panel sits at the bottom. The desktop layout is sized to fit common browser windows; smaller screens scroll naturally.

## Files

| File | Purpose |
| --- | --- |
| `index.html` | Complete landing page, including embedded styles, JavaScript, fonts, and SVG artwork. |
| `IOS Email Siganture.html` | Matching email signature with SVG icons, an SVG fundraiser panel, and an embedded PNG QR code. The existing filename is retained. |

## Features

- Email and phone links, plus copy-to-clipboard buttons.
- Downloadable vCard containing Travis Ramsey's contact information.
- GitHub, X, YouTube, Reddit, Facebook, and Truth Social links.
- GoFundMe donation link and saved fundraiser figures.
- Light/dark theme switching with a saved preference.
- Animated intro with automatic dismissal and a Skip button.
- Reduced-motion support and visible keyboard focus indicators.
- Embedded assets: no external font, image, or script downloads are required to display the page.

Social and donation links open their external destinations when selected. Fundraiser figures are a saved snapshot, not live campaign data.

## Preview locally

No installation, build step, or environment variables are required. Open `index.html` in a browser.

From PowerShell in the repository folder:

```powershell
Start-Process .\index.html
```

For an HTTP preview, if Python is installed:

```powershell
python -m http.server 8000
```

Open [localhost:8000](http://localhost:8000). Stop the server with `Ctrl+C`.

On WSL/Linux, use `python3 -m http.server 8000` instead.

## Publish with GitHub Pages

1. Open the repository's **Settings → Pages**.
2. Select **Deploy from a branch**.
3. Choose **main** and **/ (root)**, then save.
4. Wait for GitHub's deployment to finish and use the URL shown in Pages settings.

The root `index.html` is the site's entry point. No build command is needed. Once branch-based Pages publishing is configured, subsequent pushes to that branch trigger updates.

## Email signature

Open `IOS Email Siganture.html` in a browser to preview it. For an email editor that supports HTML source, use the outer signature table from the file. For a rich-text signature editor, copy the rendered signature and paste it into the editor, then send a test message.

The signature uses inline styles and tables, with SVG social/contact icons and an SVG GoFundMe panel. Email clients may remove SVG or embedded images during pasting or delivery. Browser rendering has been checked; actual iOS Mail and other email-client rendering has not been verified. Test the signature in your target client before relying on it.

## Customize

Edit `index.html` directly:

- Update contact text, `mailto:`/`tel:` links, and the vCard content together.
- Update social destinations and displayed handles together.
- Change the GoFundMe URL wherever it appears, and manually update the saved figures when needed.
- Adjust the CSS color variables for the theme.
- Edit the intro markup and its animations to change the opening reveal.

Update the signature separately so its contact information and fundraiser panel stay consistent. If the QR destination changes, replace the embedded QR image too.

## Validation

The current landing page has been checked for JavaScript syntax, desktop viewport fit, mobile horizontal overflow, theme switching, vCard downloads, intro dismissal, and reduced-motion behavior. The signature has been rendered in a browser at desktop and mobile sizes.

These checks do not verify external social accounts, live fundraiser totals, or email-client compatibility.
