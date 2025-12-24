# Notes App Feature Specification

## Executive Summary

This comprehensive feature specification for a notes application is based on extensive research including:
- Web research on the top notes apps (Notion, Evernote, Obsidian, OneNote, Apple Notes)
- Analysis of user-requested features and common complaints
- Download and analysis of 5 open-source F-Droid notes apps (Notally, Notesnook, Privacy Friendly Notes, Easy Notes, Fossify Notes)
- APK manifest analysis to understand technical capabilities and permissions

The goal is to create a notes app that balances simplicity with powerful features, respects user privacy, and provides an excellent user experience.

---

## Part 1: Apps Analyzed

### 1. Notally
- **Package**: com.omgodse.notally
- **Version**: 6.1 (versionCode 56)
- **Size**: ~2 MB
- **Min SDK**: 21 (Android 5.0)
- **Target SDK**: 34

**Permissions Required**:
- `FOREGROUND_SERVICE` - For background operations
- `FOREGROUND_SERVICE_MICROPHONE` - Audio recording
- `POST_NOTIFICATIONS` - Reminders
- `RECORD_AUDIO` - Voice notes
- `SCHEDULE_EXACT_ALARM` - Precise reminders
- `WAKE_LOCK` - Keep device awake during operations
- `RECEIVE_BOOT_COMPLETED` - Restore reminders after reboot

**Key Features** (from web research):
- Minimalist Material Design UI
- Rich text (bold, italic, monospace, strikethrough)
- Checklist support
- Image attachments (JPG, PNG, WEBP)
- Audio notes
- Note pinning and archiving
- Color labels
- Export to PDF, TXT, JSON, HTML
- Widgets
- Reminders
- Dark mode
- Auto-save and backup
- Extremely lightweight (~1.2 MB APK)

**Strengths**: Ultra-lightweight, fast launch, distraction-free, privacy-focused (no analytics)
**Weaknesses**: No cloud sync, limited formatting options, no folders (flat organization)

---

### 2. Notesnook
- **Package**: com.streetwriters.notesnook
- **Version**: 3.3.11 (versionCode 15439)
- **Size**: ~36 MB (x86_64)
- **Min SDK**: 24 (Android 7.0)
- **Target SDK**: 34

**Key Features** (from web research):
- End-to-end encryption (XChaCha20-Poly1305 & Argon2)
- Cross-platform sync (Android, iOS, Windows, Mac, Linux, Web)
- Multiple notebooks with topics
- Rich text editor with markdown shortcuts
- Todo lists, tables, images, video embeds
- Tags and color coding
- Web clipper
- Bidirectional note linking
- Offline access
- Export to PDF, HTML, Markdown, Plain Text
- Zero-knowledge architecture
- 100% open source (including sync server)

**Strengths**: Industry-leading encryption, excellent cross-platform sync, Evernote-like features
**Weaknesses**: Larger app size, requires account for sync, freemium model

---

### 3. Privacy Friendly Notes
- **Package**: org.secuso.privacyfriendlynotes
- **Version**: 2.1.1 (versionCode 102)
- **Size**: ~8 MB
- **Min SDK**: 21 (Android 5.0)
- **Target SDK**: 34

**Permissions Required**:
- `SCHEDULE_EXACT_ALARM` - Reminders
- `POST_NOTIFICATIONS` - Alerts
- `RECEIVE_BOOT_COMPLETED` - Restore after reboot
- `RECORD_AUDIO` - Voice notes

**Key Features** (from research):
- Four note types: Text, Checklist, Audio, Sketch
- Categories for organization
- Reminders
- Note export
- Minimal permissions approach
- No tracking/advertising
- No internet required
- GPLv3 licensed
- Developed by SECUSO (Karlsruhe Institute of Technology)

**Strengths**: Maximum privacy, minimal permissions, multiple note types including sketches
**Weaknesses**: No cloud sync, basic UI, limited formatting

---

### 4. Easy Notes
- **Package**: com.kin.easynotes
- **Version**: 1.4 (versionCode 9)
- **Size**: ~3.6 MB
- **Min SDK**: 26 (Android 8.0)
- **Target SDK**: 34

**Permissions Required**:
- `USE_BIOMETRIC` - Biometric authentication
- `USE_FINGERPRINT` - Fingerprint unlock

**Key Features** (from research):
- Sleek, minimalistic design
- Full Markdown support (including images)
- Secure encrypted notes vault
- Biometric authentication
- Zero permissions for basic use
- Dark mode support
- Regular updates

**Strengths**: Markdown support, biometric security, clean UI, minimal permissions
**Weaknesses**: No cloud sync, newer app (less mature)

---

### 5. Fossify Notes
- **Package**: org.fossify.notes
- **Version**: 1.6.0 (versionCode 12)
- **Size**: ~9 MB
- **Min SDK**: 26 (Android 8.0)
- **Target SDK**: 36

**Permissions Required**:
- `WRITE_EXTERNAL_STORAGE` (SDK 28 max)
- `RECEIVE_BOOT_COMPLETED`
- `WAKE_LOCK`
- `SCHEDULE_EXACT_ALARM`
- `USE_FINGERPRINT`

**Key Features** (from APK analysis):
- Multiple customizable app icon colors (20+ themes)
- Fingerprint lock support
- Widgets
- Auto-save
- Text formatting
- Dark/light themes
- Material Design 3
- Fully open source (fork of Simple Notes)
- No ads, no tracking
- Community-driven development

**Strengths**: Highly customizable appearance, reliable, community-maintained fork
**Weaknesses**: No cloud sync, basic feature set

---

## Part 2: Feature Comparison Matrix

| Feature | Notally | Notesnook | PF Notes | Easy Notes | Fossify |
|---------|:-------:|:---------:|:--------:|:----------:|:-------:|
| **Rich Text** | Yes | Yes | No | Yes* | Basic |
| **Markdown** | Partial | Yes | No | Yes | No |
| **Checklists** | Yes | Yes | Yes | Yes | Yes |
| **Images** | Yes | Yes | No | Yes | No |
| **Audio Notes** | Yes | No | Yes | No | No |
| **Sketching** | No | No | Yes | No | No |
| **Dark Mode** | Yes | Yes | Yes | Yes | Yes |
| **Cloud Sync** | No | Yes | No | No | No |
| **E2E Encryption** | No | Yes | No | Vault | No |
| **Biometric Lock** | No | Yes | No | Yes | Yes |
| **Export Options** | PDF/TXT/JSON/HTML | PDF/MD/HTML/TXT | Basic | Basic | Basic |
| **Widgets** | Yes | Partial | No | Yes | Yes |
| **Reminders** | Yes | Yes | Yes | Yes | Yes |
| **Tags/Labels** | Yes | Yes | Yes | Yes | Partial |
| **Pin Notes** | Yes | Yes | No | Yes | Yes |
| **Archive** | Yes | Yes | No | Yes | Yes |
| **Folders** | No | Yes | Yes | No | No |
| **App Size** | 2 MB | 36 MB | 8 MB | 3.6 MB | 9 MB |
| **Min Android** | 5.0 | 7.0 | 5.0 | 8.0 | 8.0 |

*Markdown with images

---

## Part 3: Recommended Features

### Tier 1: Core (MVP)

These features are essential for a minimum viable notes app:

#### Note Management
- [ ] **Create/Edit/Delete notes** - Basic CRUD operations
- [ ] **Auto-save** - Save changes automatically to prevent data loss
- [ ] **Note list view** - Show all notes with preview
- [ ] **Search** - Full-text search across all notes

#### Text Editing
- [ ] **Plain text input** - Basic text entry
- [ ] **Bold, Italic, Underline** - Essential formatting
- [ ] **Bullet/Numbered lists** - Basic organization
- [ ] **Checkboxes** - Task lists and todo items

#### Organization
- [ ] **Pin notes** - Keep important notes at top
- [ ] **Sort options** - By date modified, created, alphabetical
- [ ] **Color labels** - Visual categorization (5-8 colors)

#### UI/UX
- [ ] **Dark mode** - Essential for battery and eye comfort
- [ ] **Material Design 3** - Modern Android design language
- [ ] **Floating action button** - Quick note creation
- [ ] **Swipe gestures** - Delete/archive on swipe

### Tier 2: Important

Features that significantly improve the app experience:

#### Enhanced Editing
- [ ] **Markdown support** - For power users
- [ ] **Strikethrough** - Text decoration
- [ ] **Links** - Clickable URLs, emails, phone numbers
- [ ] **Image embedding** - Insert photos and screenshots
- [ ] **Undo/Redo** - Edit history

#### Organization
- [ ] **Tags** - Multiple tags per note (#tag syntax)
- [ ] **Folders/Notebooks** - Hierarchical organization
- [ ] **Archive** - Remove from main view without deleting
- [ ] **Trash** - Recoverable deletion (30-day retention)

#### Export & Backup
- [ ] **Export to TXT** - Universal format
- [ ] **Export to PDF** - Print-ready output
- [ ] **Export to Markdown** - Developer-friendly
- [ ] **Auto-backup** - Periodic local backup
- [ ] **Import notes** - From other apps

#### Notifications
- [ ] **Reminders** - Time-based alerts for notes
- [ ] **Widgets** - Home screen note display
- [ ] **Quick note widget** - Add notes without opening app

### Tier 3: Advanced

Features for power users and differentiation:

#### Security
- [ ] **App lock** - PIN/Password protection
- [ ] **Biometric unlock** - Fingerprint/Face
- [ ] **Encrypted notes vault** - Password-protect sensitive notes
- [ ] **End-to-end encryption** - Zero-knowledge security

#### Rich Media
- [ ] **Audio notes** - Voice recording
- [ ] **Drawing/Sketching** - Handwritten notes
- [ ] **File attachments** - PDF, documents

#### Sync & Collaboration
- [ ] **Cloud sync** - Sync across devices
- [ ] **Self-hosted option** - Privacy-focused users
- [ ] **Share notes** - Export/share to other apps
- [ ] **Collaborative editing** - Real-time multi-user

#### Power Features
- [ ] **Note linking** - Wiki-style [[links]]
- [ ] **Templates** - Pre-defined note structures
- [ ] **Version history** - Track changes over time
- [ ] **Customizable themes** - Icon colors, accent colors
- [ ] **Keyboard shortcuts** - For tablet/desktop use

---

## Part 4: Technical Recommendations

### Android Development

**Minimum SDK**: 26 (Android 8.0)
- Covers 95%+ of active devices
- Modern APIs available

**Target SDK**: 34 (Android 14)
- Required for Play Store compliance
- Access to latest features

**Architecture**:
- MVVM pattern with Android Jetpack
- Room database for local storage
- Kotlin Coroutines for async operations
- Jetpack Compose for UI (or Material Components)

### Permissions Strategy

**Required Permissions** (request only when needed):
```xml
<!-- Core functionality -->
<uses-permission android:name="android.permission.POST_NOTIFICATIONS"/>
<uses-permission android:name="android.permission.RECEIVE_BOOT_COMPLETED"/>
<uses-permission android:name="android.permission.SCHEDULE_EXACT_ALARM"/>

<!-- Optional - Audio notes -->
<uses-permission android:name="android.permission.RECORD_AUDIO"/>
<uses-permission android:name="android.permission.FOREGROUND_SERVICE_MICROPHONE"/>

<!-- Optional - Biometric lock -->
<uses-permission android:name="android.permission.USE_BIOMETRIC"/>

<!-- Optional - Export (Android 9 and below) -->
<uses-permission android:name="android.permission.WRITE_EXTERNAL_STORAGE"
    android:maxSdkVersion="28"/>
```

**Privacy Best Practices**:
- No internet permission for offline-only mode
- No analytics or tracking
- Request permissions only when needed
- Clear explanation for each permission request

### Database Schema

```sql
-- Notes table
CREATE TABLE notes (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT,
    content TEXT NOT NULL,
    type TEXT DEFAULT 'text', -- text, checklist, audio, sketch
    color TEXT DEFAULT 'default',
    is_pinned INTEGER DEFAULT 0,
    is_archived INTEGER DEFAULT 0,
    is_deleted INTEGER DEFAULT 0,
    folder_id INTEGER,
    created_at INTEGER NOT NULL,
    modified_at INTEGER NOT NULL,
    reminder_at INTEGER,
    FOREIGN KEY (folder_id) REFERENCES folders(id)
);

-- Tags table
CREATE TABLE tags (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT UNIQUE NOT NULL,
    color TEXT
);

-- Note-Tags junction
CREATE TABLE note_tags (
    note_id INTEGER,
    tag_id INTEGER,
    PRIMARY KEY (note_id, tag_id),
    FOREIGN KEY (note_id) REFERENCES notes(id),
    FOREIGN KEY (tag_id) REFERENCES tags(id)
);

-- Folders/Notebooks
CREATE TABLE folders (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    parent_id INTEGER,
    color TEXT,
    created_at INTEGER NOT NULL
);

-- Attachments
CREATE TABLE attachments (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    note_id INTEGER NOT NULL,
    type TEXT NOT NULL, -- image, audio, file
    path TEXT NOT NULL,
    size INTEGER,
    created_at INTEGER NOT NULL,
    FOREIGN KEY (note_id) REFERENCES notes(id)
);
```

---

## Part 5: UI/UX Recommendations

### Navigation Pattern

**Bottom Navigation Bar** (3 tabs):
1. **Notes** - Main note list
2. **Search** - Full-text search
3. **Settings** - App configuration

**Alternative: Single screen + Drawer**:
- Drawer for folders/tags
- Main area for note list
- FAB for new note

### Note List Screen

```
┌─────────────────────────────────┐
│ ☰  Notes           🔍  ⋮       │
├─────────────────────────────────┤
│ ┌─────────────────────────────┐ │
│ │ 📌 Pinned Note Title        │ │
│ │ Preview text here...        │ │
│ │ 🏷️ tag1  🏷️ tag2    5m ago │ │
│ └─────────────────────────────┘ │
│ ┌─────────────────────────────┐ │
│ │ 🔴 Shopping List            │ │
│ │ ☑ Milk  ☐ Bread  ☐ Eggs    │ │
│ │                       1h ago │ │
│ └─────────────────────────────┘ │
│ ┌─────────────────────────────┐ │
│ │ 🟢 Meeting Notes            │ │
│ │ Discussed Q4 targets...     │ │
│ │                     Yesterday │ │
│ └─────────────────────────────┘ │
│                                 │
│                           ➕   │ ← FAB
└─────────────────────────────────┘
```

### Editor Screen

```
┌─────────────────────────────────┐
│ ←  Note Title          💾 ⋮    │
├─────────────────────────────────┤
│ ┌─────────────────────────────┐ │
│ │ B  I  U  S  •  1.  ☑  🔗 📷│ │ ← Toolbar
│ └─────────────────────────────┘ │
│                                 │
│ Your note content goes here.   │
│ This is a sample paragraph.    │
│                                 │
│ • Bullet point 1               │
│ • Bullet point 2               │
│                                 │
│ ☑ Completed task               │
│ ☐ Pending task                 │
│                                 │
└─────────────────────────────────┘
```

### Design Principles

1. **Simplicity First** - Don't overwhelm users with options
2. **Fast Launch** - < 500ms cold start
3. **Auto-save** - Never lose user data
4. **Accessibility** - Support TalkBack, large text, high contrast
5. **Offline-first** - All core features work without internet
6. **Progressive Disclosure** - Advanced features hidden until needed

---

## Part 6: Competitive Positioning

### Market Segments

| Segment | Example Apps | Our Position |
|---------|--------------|--------------|
| Minimal | Notally, Google Keep | Lightweight option |
| Power User | Obsidian, Notion | Advanced features |
| Privacy | Standard Notes, Notesnook | E2E encryption |
| Enterprise | OneNote, Evernote | Team features |

### Recommended Positioning

**Target**: Privacy-conscious users who want a simple but capable notes app

**Differentiators**:
1. **Privacy-first** - No tracking, minimal permissions, optional E2E encryption
2. **Lightweight** - < 5MB APK, fast performance
3. **Open Source** - Full transparency, community contributions
4. **Offline-first** - No cloud required (optional sync)
5. **Modern UI** - Material Design 3, clean aesthetic

---

## Part 7: Development Roadmap

### Phase 1: MVP
- Basic note creation, editing, deletion
- Search and organization (pin, archive, colors)
- Auto-save and basic export
- Dark mode and Material Design 3 UI

### Phase 2: Enhanced Editing
- Markdown support
- Image attachments
- Checklists with proper UI
- Tags system
- Reminders and widgets

### Phase 3: Security & Sync
- App lock (PIN/biometric)
- Encrypted notes vault
- Cloud sync (optional)
- Import from other apps

### Phase 4: Power Features
- Audio notes
- Drawing/sketching
- Note linking
- Templates
- Collaborative editing

---

## Appendix A: APK Analysis Summary

| App | Package | Version | Size | Permissions |
|-----|---------|---------|------|-------------|
| Notally | com.omgodse.notally | 6.1 | 2.0 MB | 7 |
| Notesnook | com.streetwriters.notesnook | 3.3.11 | 36 MB | Many* |
| PF Notes | org.secuso.privacyfriendlynotes | 2.1.1 | 8.4 MB | 4 |
| Easy Notes | com.kin.easynotes | 1.4 | 3.6 MB | 2 |
| Fossify Notes | org.fossify.notes | 1.6.0 | 9.4 MB | 5 |

*Notesnook requires more permissions for sync and encryption features

---

## Appendix B: Research Sources

### Web Research
- [Zapier - Best Note-Taking Apps](https://zapier.com/blog/best-note-taking-apps/)
- [NoteApps.info - Feature Comparison](https://noteapps.info/apps/compare)
- [MakeUseOf - Open Source Notes Apps](https://www.makeuseof.com/tag/5-best-open-source-note-taking-apps-android/)
- [DEV Community - Feature Discussion](https://dev.to/z3r0tw0_zt/what-are-all-the-features-you-look-for-in-a-note-taking-app-4klg)

### F-Droid App Pages
- [Notally](https://f-droid.org/packages/com.omgodse.notally/)
- [Notesnook](https://f-droid.org/packages/com.streetwriters.notesnook/)
- [Privacy Friendly Notes](https://f-droid.org/packages/org.secuso.privacyfriendlynotes/)
- [Easy Notes](https://f-droid.org/packages/com.kin.easynotes/)
- [Fossify Notes](https://f-droid.org/packages/org.fossify.notes/)

### Official Documentation
- [GitHub - Notally](https://github.com/OmGodse/Notally)
- [GitHub - Notesnook](https://github.com/streetwriters/notesnook)
- [Notesnook.com](https://notesnook.com/)
- [Standard Notes](https://standardnotes.com/features)

---

*Document generated: December 2024*
*Research by: AI Agent*
