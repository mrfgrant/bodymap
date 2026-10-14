# Where Do I Start (PWA)

Static files. Host them on any HTTPS server (Vercel, Netlify, Replit static, S3). No build step.

- index.html   the app, images embedded
- manifest.webmanifest   name, icons, standalone display
- sw.js   offline shell; change VERSION on every deploy so phones pick up the new build
- icons/   192, 512, maskable 512, Apple touch 180

Install: Android shows an Install button in the app. iPhone: Share, then Add to Home Screen (the app shows a one-time tip).
Progress saves on the device and resumes on next open. Nothing leaves the phone until "Send to a reviewer", which is still a mock.

Vercel: `npx vercel --prod` from this folder, or drag the folder onto vercel.com/new.
