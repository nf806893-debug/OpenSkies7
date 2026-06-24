# 🌤 OpenSkies7

[insert link future me]

A clean, iOS 7-inspired weather Progressive Web App (PWA) powered by the free [Open-Meteo API](https://open-meteo.com/). No API key required.


## Features

- 🌍 **Auto-location** — detects your location via GPS
- 🔍 **City search** — search any city worldwide
- 🌡 **°C / °F toggle**
- 📅 **7-day forecast** with temperature range bars
- ⏱ **24-hour hourly forecast**
- 💧 Humidity, wind, visibility, pressure
- 🌅 Sunrise / sunset times, UV index, precipitation
- 🎨 **Dynamic backgrounds** — changes by weather type and time of day (day, sunrise, sunset, night)
- ⭐ Animated particles — stars at night, rain during storms, snow in winter
- 📱 **Installable PWA** — add to home screen on iOS or Android
- ✈️ **Offline-ready** — app shell loads without internet

## Compatibility

| Platform | Version | Notes |
|---|---|---|
| iOS Safari | 7+ | untested - let me know if it does. |
| Android Chrome | 4.4+ | untested - let me know if it does. |
| Modern browsers | All | Works, I mean obviously. |

> Written in **ES5-compatible vanilla JS** — no build tools, no bundler, no Node.js required. A single `index.html` runs the whole app.

## Getting Started

### Option 1 — Just open the file

Double-click `index.html` in your file browser. Done.

> ⚠️ Geolocation may not work on `file://` URLs in some browsers. Use a local server for best results.

### Option 2 — Local server (recommended)

If you have Python installed:

```bash
# Python 3
python3 -m http.server 8080

# Python 2
python -m SimpleHTTPServer 8080
```

Then open `http://localhost:8080` in your browser.

Or with Node.js:

```bash
npx serve .
```

### Option 3 — Deploy for free

| Host | Steps |
|---|---|
| **GitHub Pages** | Push to a repo → Settings → Pages → Deploy from `main` branch |
| **Netlify** | Drag & drop the folder at [app.netlify.com](https://app.netlify.com) |
| **Vercel** | `npx vercel` in the folder |

## Installing on iOS (Add to Home Screen)

1. Open the hosted URL in **Safari** (must be HTTPS or localhost for PWA features)
2. Tap the **Share** button (box with arrow)
3. Tap **"Add to Home Screen"**
4. The app opens full-screen with no browser UI

## File Structure

```
weather-app/
├── index.html          # Entire app — HTML, CSS, and JS in one file
├── manifest.json       # PWA manifest (icons, name, theme)
├── sw.js               # Service worker (offline caching)
├── generate-icons.py   # Run once to generate app icons (needs Pillow)
├── icons/
│   ├── icon-152.png    # iPad home screen icon
│   ├── icon-167.png    # iPad Pro home screen icon
│   ├── icon-180.png    # iPhone home screen icon
│   ├── icon-192.png    # Android / PWA icon
│   └── icon-512.png    # PWA splash / store icon
└── README.md
```

## Generating Icons

If you need to regenerate the icons:

```bash
pip install pillow
python3 generate-icons.py
```

## APIs Used

| API | Purpose | Cost |
|---|---|---|
| [Open-Meteo](https://open-meteo.com/) | Weather data & forecasts | Free, no key |
| [Open-Meteo Geocoding](https://open-meteo.com/en/docs/geocoding-api) | City search | Free, no key |
| [Nominatim (OSM)](https://nominatim.openstreetmap.org/) | Reverse geocoding (GPS → city name) | Free, no key |

## License

MIT — do whatever you want with it.
