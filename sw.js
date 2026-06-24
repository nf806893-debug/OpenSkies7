/* ================================================================
   SERVICE WORKER — Weather PWA
   Caches the app shell for offline loading.
   Weather data always fetches fresh (network-first).
================================================================ */

var CACHE_NAME = 'weather-app-v1';
var SHELL_FILES = [
  '/',
  '/index.html',
  '/manifest.json'
];

// Install — cache the app shell
self.addEventListener('install', function(event) {
  event.waitUntil(
    caches.open(CACHE_NAME).then(function(cache) {
      return cache.addAll(SHELL_FILES);
    })
  );
  self.skipWaiting();
});

// Activate — clean up old caches
self.addEventListener('activate', function(event) {
  event.waitUntil(
    caches.keys().then(function(keys) {
      return Promise.all(
        keys.filter(function(key) {
          return key !== CACHE_NAME;
        }).map(function(key) {
          return caches.delete(key);
        })
      );
    })
  );
  return self.clients.claim();
});

// Fetch strategy:
// - API calls → network first, no cache
// - App shell → cache first, fallback to network
self.addEventListener('fetch', function(event) {
  var url = event.request.url;

  // Always go to network for API and geocoding calls
  if (url.indexOf('open-meteo.com') !== -1 ||
      url.indexOf('nominatim.openstreetmap.org') !== -1) {
    event.respondWith(fetch(event.request));
    return;
  }

  // App shell: cache first
  event.respondWith(
    caches.match(event.request).then(function(cached) {
      return cached || fetch(event.request).then(function(response) {
        // Cache new shell files as they're fetched
        var clone = response.clone();
        caches.open(CACHE_NAME).then(function(cache) {
          cache.put(event.request, clone);
        });
        return response;
      });
    })
  );
});
