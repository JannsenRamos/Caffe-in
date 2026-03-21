<!-- Design System -->
<!DOCTYPE html>

<html lang="en"><head>
<meta charset="utf-8"/>
<meta content="width=device-width, initial-scale=1.0" name="viewport"/>
<title>Caffe-In | Your Coffee Sommelier</title>
<script src="https://cdn.tailwindcss.com?plugins=forms,container-queries"></script>
<link href="https://fonts.googleapis.com/css2?family=Newsreader:ital,opsz,wght@0,6..72,200..800;1,6..72,200..800&amp;family=Plus+Jakarta+Sans:wght@200..800&amp;family=IBM+Plex+Mono:wght@400;500&amp;family=Material+Symbols+Outlined:wght,FILL@100..700,0..1&amp;display=swap" rel="stylesheet"/>
<link href="https://fonts.googleapis.com/css2?family=Material+Symbols+Outlined:wght,FILL@100..700,0..1&amp;display=swap" rel="stylesheet"/>
<script id="tailwind-config">
        tailwind.config = {
            darkMode: "class",
            theme: {
                extend: {
                    colors: {
                        "tertiary": "#174a2b",
                        "surface-container-high": "#ece8e0",
                        "primary-fixed-dim": "#ffb68c",
                        "on-tertiary": "#ffffff",
                        "inverse-surface": "#32302b",
                        "on-primary-container": "#ffc29f",
                        "surface": "#fef9f1",
                        "surface-container-highest": "#e7e2da",
                        "on-secondary": "#ffffff",
                        "on-primary": "#ffffff",
                        "outline-variant": "#dac2b6",
                        "secondary": "#934b00",
                        "on-tertiary-fixed": "#00210e",
                        "primary": "#6c2f00",
                        "on-background": "#1d1c17",
                        "on-secondary-fixed": "#301400",
                        "on-error-container": "#93000a",
                        "surface-container": "#f2ede5",
                        "outline": "#877369",
                        "on-surface": "#1d1c17",
                        "tertiary-fixed-dim": "#9dd3aa",
                        "secondary-fixed-dim": "#ffb781",
                        "surface-container-lowest": "#ffffff",
                        "on-primary-fixed": "#321200",
                        "error-container": "#ffdad6",
                        "tertiary-container": "#316241",
                        "on-error": "#ffffff",
                        "secondary-container": "#fea054",
                        "inverse-on-surface": "#f5f0e8",
                        "primary-fixed": "#ffdbc9",
                        "inverse-primary": "#ffb68c",
                        "surface-variant": "#e7e2da",
                        "secondary-fixed": "#ffdcc5",
                        "error": "#ba1a1a",
                        "on-secondary-fixed-variant": "#703800",
                        "surface-bright": "#fef9f1",
                        "surface-tint": "#934b19",
                        "on-primary-fixed-variant": "#753401",
                        "tertiary-fixed": "#b9efc5",
                        "background": "#fef9f1",
                        "on-tertiary-fixed-variant": "#1e5031",
                        "on-secondary-container": "#703800",
                        "surface-dim": "#ded9d2",
                        "on-surface-variant": "#54433a",
                        "on-tertiary-container": "#a6dcb2",
                        "primary-container": "#8b4513",
                        "surface-container-low": "#f8f3eb"
                    },
                    fontFamily: {
                        "headline": ["Newsreader", "serif"],
                        "body": ["Plus Jakarta Sans", "sans-serif"],
                        "label": ["Plus Jakarta Sans", "sans-serif"],
                        "mono": ["IBM Plex Mono", "monospace"]
                    },
                    borderRadius: {
                        "DEFAULT": "1rem",
                        "lg": "2rem",
                        "xl": "3rem",
                        "full": "9999px"
                    },
                },
            },
        }
    </script>
<style>
        .topo-bg {
            background-image: url("data:image/svg+xml,%3Csvg width='800' height='800' viewBox='0 0 800 800' xmlns='http://www.w3.org/2000/svg'%3E%3Cpath d='M0 799c15.6-2.5 31.2-5 46.8-7.5 15.6-2.5 31.2-5 46.8-7.5 15.6-2.5 31.2-5 46.8-7.5m100-100c20-5 40-10 60-15s40-10 60-15c20-5 40-10 60-15m-300 200c50-10 100-20 150-30s100-20 150-30c50-10 100-20 150-30' fill='none' stroke='%236c2f00' stroke-opacity='0.03' stroke-width='1'/%3E%3C/svg%3E");
            background-size: 600px 600px;
        }
        .material-symbols-outlined {
            font-variation-settings: 'FILL' 0, 'wght' 400, 'GRAD' 0, 'opsz' 24;
        }
    </style>
</head>
<body class="bg-surface text-on-surface font-body selection:bg-primary-fixed selection:text-on-primary-fixed topo-bg min-h-screen">
<!-- Top Navigation Bar -->
<header class="bg-[#fef9f1] dark:bg-stone-950 font-serif text-lg tracking-tight Newsreader docked full-width top-0 no-border space-y-8 bg-transparent flat no shadows">
<nav class="flex justify-between items-center w-full px-12 py-6 max-w-screen-2xl mx-auto">
<div class="font-serif italic text-2xl text-[#1d1c17] dark:text-stone-100">
                Caffe-In
            </div>
<div class="hidden md:flex items-center gap-10">
<a class="text-[#1d1c17]/60 dark:text-stone-400 font-medium hover:text-[#6c2f00] transition-colors duration-300" href="#">Curations</a>
<a class="text-[#1d1c17]/60 dark:text-stone-400 font-medium hover:text-[#6c2f00] transition-colors duration-300" href="#">Roasters</a>
<a class="text-[#1d1c17]/60 dark:text-stone-400 font-medium hover:text-[#6c2f00] transition-colors duration-300" href="#">Journal</a>
</div>
<div class="flex items-center gap-6">
<button class="text-[#1d1c17]/60 dark:text-stone-400 hover:text-[#6c2f00] transition-colors duration-300">
<span class="material-symbols-outlined">account_circle</span>
</button>
</div>
</nav>
</header>
<!-- Main Hero Section -->
<main class="relative flex flex-col items-center justify-center pt-24 pb-32 px-6 max-w-screen-xl mx-auto overflow-hidden">
<!-- Hero Content -->
<div class="text-center z-10 max-w-3xl">
<h1 class="font-headline text-6xl md:text-8xl tracking-tight leading-tight text-on-background mb-8 italic">
                Describe your perfect cup.
            </h1>
<p class="font-body text-xl md:text-2xl text-on-surface-variant font-light mb-12 leading-relaxed">
                Caffe-In finds coffees that match your flavor language — and tells you how confident to be in the pick.
            </p>
</div>
<!-- Search Experience -->
<div class="w-full max-w-2xl z-10 space-y-8">
<div class="relative group">
<div class="absolute -inset-4 bg-primary/5 rounded-full blur-2xl opacity-0 group-focus-within:opacity-100 transition-opacity duration-700"></div>
<div class="relative flex items-center bg-surface-container-lowest rounded-full p-2 shadow-[0px_12px_32px_rgba(29,28,23,0.06)] border border-outline-variant/20 focus-within:border-primary/30 transition-all duration-300">
<input class="w-full bg-transparent border-none focus:ring-0 px-8 py-4 text-lg text-on-surface placeholder:text-on-surface-variant/40 font-body" placeholder="e.g., bright citrus floral light roast..." type="text"/>
<button class="bg-secondary hover:bg-primary text-on-secondary px-8 py-4 rounded-full font-medium flex items-center gap-2 transition-all duration-300 whitespace-nowrap">
                        Find my coffee
                        <span class="material-symbols-outlined text-sm">arrow_forward</span>
</button>
</div>
</div>
<!-- Roast Filters -->
<div class="flex flex-wrap justify-center gap-3">
<button class="px-5 py-2 rounded-full border border-primary text-primary text-sm font-medium transition-colors bg-primary/5">All</button>
<button class="px-5 py-2 rounded-full border border-outline-variant/30 text-on-surface-variant text-sm font-medium hover:border-primary/50 hover:bg-surface-container-low transition-colors">Light</button>
<button class="px-5 py-2 rounded-full border border-outline-variant/30 text-on-surface-variant text-sm font-medium hover:border-primary/50 hover:bg-surface-container-low transition-colors">Medium</button>
<button class="px-5 py-2 rounded-full border border-outline-variant/30 text-on-surface-variant text-sm font-medium hover:border-primary/50 hover:bg-surface-container-low transition-colors">Dark</button>
<button class="px-5 py-2 rounded-full border border-outline-variant/30 text-on-surface-variant text-sm font-medium hover:border-primary/50 hover:bg-surface-container-low transition-colors">Espresso</button>
</div>
</div>
<!-- Decorative Elements -->
<div class="absolute top-0 right-0 -mr-24 opacity-20 pointer-events-none">
<div class="w-96 h-96 bg-primary-fixed-dim rounded-full blur-3xl"></div>
</div>
<div class="absolute bottom-0 left-0 -ml-24 opacity-10 pointer-events-none">
<div class="w-64 h-64 bg-tertiary-fixed rounded-full blur-3xl"></div>
</div>
</main>
<!-- How It Works Section -->
<section class="bg-surface-container-low py-32 px-12 md:px-24">
<div class="max-w-screen-xl mx-auto">
<div class="flex flex-col md:flex-row gap-16 md:gap-8 items-start">
<!-- Step 1 -->
<div class="flex-1 space-y-6">
<div class="font-mono text-sm tracking-widest uppercase text-primary/60">Phase 01</div>
<h3 class="font-headline text-3xl text-on-background">Describe in Plain English</h3>
<p class="font-body text-on-surface-variant leading-relaxed">
                        No need for technical cupping scores. Tell us what you like—"smoky morning brew" or "acidic afternoon berry notes"—and our model parses the intent.
                    </p>
<div class="h-px w-full bg-outline-variant/30"></div>
</div>
<!-- Step 2 -->
<div class="flex-1 space-y-6">
<div class="font-mono text-sm tracking-widest uppercase text-primary/60">Phase 02</div>
<h3 class="font-headline text-3xl text-on-background">The Confidence Filter</h3>
<p class="font-body text-on-surface-variant leading-relaxed">
                        We don't just show matches; we show probability. If we're 94% sure you'll love a roast, we flag it. If it's a "wildcard" choice, we let you know.
                    </p>
<div class="h-px w-full bg-outline-variant/30"></div>
</div>
<!-- Step 3 -->
<div class="flex-1 space-y-6">
<div class="font-mono text-sm tracking-widest uppercase text-primary/60">Phase 03</div>
<h3 class="font-headline text-3xl text-on-background">Editorial Context</h3>
<p class="font-body text-on-surface-variant leading-relaxed">
                        Read independent journals and roaster stories before you commit. We curate the narrative behind the bean so you know the craft you're drinking.
                    </p>
<div class="h-px w-full bg-outline-variant/30"></div>
</div>
</div>
</div>
</section>
<!-- Content Showcase: Featured Roaster (Asymmetric Layout) -->
<section class="py-32 px-12 max-w-screen-2xl mx-auto overflow-hidden">
<div class="grid grid-cols-1 md:grid-cols-12 gap-12 items-center">
<div class="md:col-span-7 relative">
<div class="aspect-[4/5] rounded-lg overflow-hidden bg-surface-container-highest shadow-xl">
<img alt="Minimalist coffee setup" class="w-full h-full object-cover grayscale-[20%] mix-blend-multiply opacity-90" data-alt="Modern minimalist aesthetic coffee cup on stone surface" src="https://lh3.googleusercontent.com/aida-public/AB6AXuDD0MWSTmUbSKvyiJcIcP6Vf-imhqqVZ1POxGzrK5fxCaBumL8CRdAJscRksHPRrMq2qSdULL-Wi953JvjC0o3S8SebWz9nd7Za7wbqcHJ4t1iRlOs6uvC4UKkQBB5RmbvyElXli7jxrtnMP-YX9dUEsno38ZupLtFAGN6kAUv4Cwi1lUBbugEAXqBONqzmBSxPdaBTGcDQ_R_TVlOmoBuejEtqrOLZetQkU0Vua0BUNeFSSl9naLyEuAybN2rheICwOH_Abs_lI6g"/>
</div>
<!-- Offset Badge -->
<div class="absolute -bottom-10 -right-10 bg-primary-container p-12 rounded-lg text-on-primary-container hidden lg:block max-w-xs shadow-2xl">
<span class="font-mono text-xs block mb-4 uppercase tracking-[0.2em]">Origin Highlight</span>
<h4 class="font-headline text-4xl mb-6">Ethiopia Yirgacheffe</h4>
<p class="font-body text-sm opacity-80 leading-relaxed">A standard-bearer for floral, tea-like washed coffees, offering profound jasmine and lemon zest aromas.</p>
</div>
</div>
<div class="md:col-span-5 md:pl-16">
<h2 class="font-headline text-5xl text-on-background mb-8 italic">The Journal of Origin</h2>
<p class="font-body text-lg text-on-surface-variant mb-10 leading-relaxed">
                    Coffee is more than a caffeine delivery system. It is a story of soil, altitude, and the meticulous hands that harvest every cherry. We track the journey from the station to your ceramic.
                </p>
<div class="flex gap-4">
<div class="flex flex-col">
<span class="font-mono text-xs text-primary font-bold uppercase">Confidence</span>
<span class="text-3xl font-headline italic">High Yield</span>
</div>
<div class="w-px h-12 bg-outline-variant/40 mx-4"></div>
<div class="flex flex-col">
<span class="font-mono text-xs text-primary font-bold uppercase">Season</span>
<span class="text-3xl font-headline italic">Peak Bloom</span>
</div>
</div>
<button class="mt-12 group flex items-center gap-4 font-headline text-2xl text-primary hover:text-secondary transition-colors">
                    Read the Editorial
                    <span class="w-12 h-px bg-primary group-hover:bg-secondary group-hover:w-16 transition-all"></span>
</button>
</div>
</div>
</section>
<!-- Minimalist Footer -->
<footer class="bg-[#f8f3eb] dark:bg-stone-900 font-sans text-xs uppercase tracking-widest Plus Jakarta Sans full-width py-12 no-border bg-[#f8f3eb] flat">
<div class="flex flex-col md:flex-row justify-between items-center px-16 w-full max-w-screen-2xl mx-auto space-y-6 md:space-y-0">
<div class="text-[#1d1c17]/50 dark:text-stone-500">
                © 2024 Caffe-In Editorial. All Rights Reserved.
            </div>
<div class="flex gap-12">
<a class="text-[#1d1c17]/50 dark:text-stone-500 hover:text-[#6c2f00] dark:hover:text-orange-300 transition-colors" href="#">The Ethos</a>
<a class="text-[#1d1c17]/50 dark:text-stone-500 hover:text-[#6c2f00] dark:hover:text-orange-300 transition-colors" href="#">Privacy</a>
<a class="text-[#1d1c17]/50 dark:text-stone-500 hover:text-[#6c2f00] dark:hover:text-orange-300 transition-colors" href="#">Contact</a>
</div>
</div>
</footer>
</body></html>

<!-- Caffe-In | Landing -->
<!DOCTYPE html>

<html lang="en"><head>
<meta charset="utf-8"/>
<meta content="width=device-width, initial-scale=1.0" name="viewport"/>
<script src="https://cdn.tailwindcss.com?plugins=forms,container-queries"></script>
<link href="https://fonts.googleapis.com/css2?family=Newsreader:ital,opsz,wght@0,6..72,200..800;1,6..72,200..800&amp;family=Plus+Jakarta+Sans:wght@200..800&amp;family=IBM+Plex+Mono:wght@400;500&amp;display=swap" rel="stylesheet"/>
<link href="https://fonts.googleapis.com/css2?family=Material+Symbols+Outlined:wght,FILL@100..700,0..1&amp;display=swap" rel="stylesheet"/>
<link href="https://fonts.googleapis.com/css2?family=Material+Symbols+Outlined:wght,FILL@100..700,0..1&amp;display=swap" rel="stylesheet"/>
<script id="tailwind-config">
      tailwind.config = {
        darkMode: "class",
        theme: {
          extend: {
            colors: {
              "tertiary": "#174a2b",
              "surface-container-high": "#ece8e0",
              "primary-fixed-dim": "#ffb68c",
              "on-tertiary": "#ffffff",
              "inverse-surface": "#32302b",
              "on-primary-container": "#ffc29f",
              "surface": "#fef9f1",
              "surface-container-highest": "#e7e2da",
              "on-secondary": "#ffffff",
              "on-primary": "#ffffff",
              "outline-variant": "#dac2b6",
              "secondary": "#934b00",
              "on-tertiary-fixed": "#00210e",
              "primary": "#6c2f00",
              "on-background": "#1d1c17",
              "on-secondary-fixed": "#301400",
              "on-error-container": "#93000a",
              "surface-container": "#f2ede5",
              "outline": "#877369",
              "on-surface": "#1d1c17",
              "tertiary-fixed-dim": "#9dd3aa",
              "secondary-fixed-dim": "#ffb781",
              "surface-container-lowest": "#ffffff",
              "on-primary-fixed": "#321200",
              "error-container": "#ffdad6",
              "tertiary-container": "#316241",
              "on-error": "#ffffff",
              "secondary-container": "#fea054",
              "inverse-on-surface": "#f5f0e8",
              "primary-fixed": "#ffdbc9",
              "inverse-primary": "#ffb68c",
              "surface-variant": "#e7e2da",
              "secondary-fixed": "#ffdcc5",
              "error": "#ba1a1a",
              "on-secondary-fixed-variant": "#703800",
              "surface-bright": "#fef9f1",
              "surface-tint": "#934b19",
              "on-primary-fixed-variant": "#753401",
              "tertiary-fixed": "#b9efc5",
              "background": "#fef9f1",
              "on-tertiary-fixed-variant": "#1e5031",
              "on-secondary-container": "#703800",
              "surface-dim": "#ded9d2",
              "on-surface-variant": "#54433a",
              "on-tertiary-container": "#a6dcb2",
              "primary-container": "#8b4513",
              "surface-container-low": "#f8f3eb"
            },
            fontFamily: {
              "headline": ["Newsreader", "serif"],
              "body": ["Plus Jakarta Sans", "sans-serif"],
              "label": ["Plus Jakarta Sans", "sans-serif"],
              "mono": ["IBM Plex Mono", "monospace"]
            },
            borderRadius: {"DEFAULT": "1rem", "lg": "2rem", "xl": "3rem", "full": "9999px"},
          },
        },
      }
    </script>
<style>
      .material-symbols-outlined {
        font-variation-settings: 'FILL' 0, 'wght' 400, 'GRAD' 0, 'opsz' 24;
      }
      .custom-scrollbar::-webkit-scrollbar {
        width: 4px;
      }
      .custom-scrollbar::-webkit-scrollbar-track {
        background: transparent;
      }
      .custom-scrollbar::-webkit-scrollbar-thumb {
        background: #dac2b6;
        border-radius: 10px;
      }
    </style>
</head>
<body class="bg-surface text-on-surface font-body selection:bg-primary-fixed selection:text-on-primary-fixed">
<!-- Top Navigation Shell -->
<nav class="sticky top-0 z-50 bg-surface/80 backdrop-blur-xl">
<div class="flex justify-between items-center w-full px-12 py-6 max-w-screen-2xl mx-auto">
<div class="font-serif italic text-2xl text-[#1d1c17] dark:text-stone-100 font-serif Newsreader">Caffe-In</div>
<div class="hidden md:flex items-center space-x-8">
<a class="text-[#1d1c17]/60 dark:text-stone-400 font-medium hover:text-[#6c2f00] transition-colors duration-300" href="#">Curations</a>
<a class="text-[#1d1c17]/60 dark:text-stone-400 font-medium hover:text-[#6c2f00] transition-colors duration-300" href="#">Roasters</a>
<a class="text-[#1d1c17]/60 dark:text-stone-400 font-medium hover:text-[#6c2f00] transition-colors duration-300" href="#">Journal</a>
</div>
<div class="flex items-center space-x-6">
<div class="relative group hidden sm:block">
<span class="absolute left-3 top-1/2 -translate-y-1/2 material-symbols-outlined text-on-surface-variant text-sm">search</span>
<input class="bg-surface-container-low border-none border-b-2 border-outline-variant focus:border-primary focus:ring-0 text-sm py-2 pl-10 pr-4 w-64 font-body tracking-tight rounded-none placeholder:text-on-surface-variant/50" type="text" value="bright citrus floral light roast"/>
</div>
<button class="material-symbols-outlined text-on-surface transition-opacity active:opacity-80">account_circle</button>
</div>
</div>
</nav>
<!-- Content Canvas -->
<main class="max-w-screen-2xl mx-auto px-12 pb-24 space-y-12">
<!-- Filter Bar -->
<header class="space-y-8 pt-8">
<div class="flex flex-col md:flex-row md:items-end justify-between gap-6">
<div class="space-y-4">
<span class="font-mono text-[10px] uppercase tracking-[0.2em] text-on-surface-variant">Roast Intensity</span>
<div class="flex flex-wrap gap-2">
<button class="px-6 py-2 rounded-full text-sm font-medium bg-surface-container-high text-on-surface hover:bg-surface-container-highest transition-colors">Extra Light</button>
<button class="px-6 py-2 rounded-full text-sm font-medium bg-primary text-on-primary ring-4 ring-primary-fixed/30 transition-shadow">Light</button>
<button class="px-6 py-2 rounded-full text-sm font-medium bg-surface-container-high text-on-surface hover:bg-surface-container-highest transition-colors">Medium</button>
<button class="px-6 py-2 rounded-full text-sm font-medium bg-surface-container-high text-on-surface hover:bg-surface-container-highest transition-colors">Dark</button>
</div>
</div>
<div class="flex items-center space-x-6">
<div class="flex flex-col items-end space-y-2">
<span class="font-mono text-[10px] uppercase tracking-[0.2em] text-on-surface-variant">Adventure Level</span>
<div class="flex bg-surface-container-low p-1 rounded-full border border-outline-variant/15">
<button class="px-5 py-1.5 rounded-full text-xs font-semibold text-on-surface-variant">Curated</button>
<button class="px-5 py-1.5 rounded-full text-xs font-bold bg-surface-container-highest text-on-surface shadow-sm">Show All</button>
</div>
</div>
</div>
</div>
</header>
<!-- Search Results Grid -->
<section class="grid grid-cols-1 md:grid-cols-2 gap-10">
<!-- Result Card 1 -->
<article class="group relative flex flex-col bg-surface-container-lowest rounded-lg p-10 transition-all duration-500 hover:shadow-[0px_12px_32px_rgba(29,28,23,0.06)] hover:ring-1 hover:ring-secondary/30">
<div class="flex justify-between items-start mb-6">
<div class="space-y-1">
<h3 class="font-headline text-3xl text-on-surface leading-tight">Yirgacheffe Gedeb</h3>
<p class="font-label text-[10px] uppercase tracking-widest text-on-surface-variant font-bold">Chelchele Station • Proud Mary Roasters</p>
</div>
<span class="px-3 py-1 bg-surface-container-high text-[10px] font-bold uppercase tracking-wider rounded-full">Light</span>
</div>
<div class="aspect-[4/3] w-full overflow-hidden rounded-lg mb-8 bg-surface-container">
<img class="w-full h-full object-cover transition-transform duration-700 group-hover:scale-105 opacity-90" data-alt="Close up of light roast coffee beans on a ceramic plate" src="https://lh3.googleusercontent.com/aida-public/AB6AXuDw2Fg-T55ryRVapNZU8A5xU6PvFsARQZdjKLkWpug2ydanCznlXgUysJfYHEtStkX0EBJIFC-jxYk5h1rEasl64nmpDvNbLMMFmNZcGNXWrtP_kLA7-bAQfG1NQMm7ruGNVRd_vgMXv0RlneMS5Yb4_KlOjKUCWS-N6zTToH5peRan6sSk8vZ-DM0WWGE_r-Jiwj_eRD8eOkZ6TEP4tEhafHhTeNyuVfPHKTFY4x6AQbWwBdfEsXO6X8bvrdFXIPQO0JtyvmDVQgs"/>
</div>
<blockquote class="font-headline italic text-xl text-on-surface-variant leading-relaxed mb-8 pr-4">
                    "A crisp, zesty profile with hints of bergamot and jasmine, reminiscent of a delicate Earl Grey tea with a honey-sweet finish."
                </blockquote>
<div class="mt-auto space-y-6">
<div class="space-y-2">
<div class="flex justify-between items-end">
<span class="font-label text-xs font-semibold text-on-surface">Flavor Match</span>
<span class="font-mono text-sm font-medium text-secondary">88.5%</span>
</div>
<div class="h-0.5 w-full bg-surface-container-high rounded-full overflow-hidden">
<div class="h-full bg-secondary w-[88.5%] transition-all duration-1000"></div>
</div>
</div>
<div class="flex justify-between items-center">
<div class="flex items-center space-x-2 px-3 py-1.5 bg-tertiary/5 rounded-full">
<span class="w-2 h-2 rounded-full bg-tertiary"></span>
<span class="text-xs font-semibold text-tertiary">Low Risk — Consistent, predictable</span>
</div>
<a class="text-xs font-semibold underline underline-offset-4 decoration-outline-variant hover:decoration-secondary transition-colors" href="#">Why this match?</a>
</div>
</div>
</article>
<!-- Result Card 2 -->
<article class="group relative flex flex-col bg-surface-container-lowest rounded-lg p-10 transition-all duration-500 hover:shadow-[0px_12px_32px_rgba(29,28,23,0.06)] hover:ring-1 hover:ring-secondary/30">
<div class="flex justify-between items-start mb-6">
<div class="space-y-1">
<h3 class="font-headline text-3xl text-on-surface leading-tight">La Palma y El Tucan</h3>
<p class="font-label text-[10px] uppercase tracking-widest text-on-surface-variant font-bold">Cundinamarca • Onyx Coffee Lab</p>
</div>
<span class="px-3 py-1 bg-surface-container-high text-[10px] font-bold uppercase tracking-wider rounded-full">Light</span>
</div>
<div class="aspect-[4/3] w-full overflow-hidden rounded-lg mb-8 bg-surface-container">
<img class="w-full h-full object-cover transition-transform duration-700 group-hover:scale-105 opacity-90" data-alt="Artistic pour over coffee setup in a bright minimalist cafe" src="https://lh3.googleusercontent.com/aida-public/AB6AXuAPb3iE4fdNy9cqkDCY2Etetu1kMK7XNSE3KY0ErXJAH9XQHdMPg6U7vsXopfTpNtDgYwVa2ftC0V9r8sCqGljN97DpDBTd0sKEZigIXertZ9hOCOd1BEHolvnSeBqHtk5lz9tDNyJGTJ2jHtvC3_z4yEx9CaCmbRjXViIyhRYCLWFrVeRadD8rP_lMTHztC_kkglrm9MiiLI39m7WAD6QKI4JMwGTOeKjUshtqM6xucONBfl3onvCUwhv5OEv5pyHrNq8UMQVcM2g"/>
</div>
<blockquote class="font-headline italic text-xl text-on-surface-variant leading-relaxed mb-8 pr-4">
                    "Vibrant acidity meets floral complexity. Expect a structured body with notes of white peach, lavender, and a sparkling citrus acidity."
                </blockquote>
<div class="mt-auto space-y-6">
<div class="space-y-2">
<div class="flex justify-between items-end">
<span class="font-label text-xs font-semibold text-on-surface">Flavor Match</span>
<span class="font-mono text-sm font-medium text-secondary">92.1%</span>
</div>
<div class="h-0.5 w-full bg-surface-container-high rounded-full overflow-hidden">
<div class="h-full bg-secondary w-[92.1%] transition-all duration-1000"></div>
</div>
</div>
<div class="flex justify-between items-center">
<div class="flex items-center space-x-2 px-3 py-1.5 bg-tertiary/5 rounded-full">
<span class="w-2 h-2 rounded-full bg-tertiary"></span>
<span class="text-xs font-semibold text-tertiary">Low Risk — Consistent, predictable</span>
</div>
<a class="text-xs font-semibold underline underline-offset-4 decoration-outline-variant hover:decoration-secondary transition-colors" href="#">Why this match?</a>
</div>
</div>
</article>
<!-- Result Card 3 -->
<article class="group relative flex flex-col bg-surface-container-lowest rounded-lg p-10 transition-all duration-500 hover:shadow-[0px_12px_32px_rgba(29,28,23,0.06)] hover:ring-1 hover:ring-secondary/30">
<div class="flex justify-between items-start mb-6">
<div class="space-y-1">
<h3 class="font-headline text-3xl text-on-surface leading-tight">Pink Bourbon</h3>
<p class="font-label text-[10px] uppercase tracking-widest text-on-surface-variant font-bold">Huila • Sey Coffee</p>
</div>
<span class="px-3 py-1 bg-surface-container-high text-[10px] font-bold uppercase tracking-wider rounded-full">Light</span>
</div>
<div class="aspect-[4/3] w-full overflow-hidden rounded-lg mb-8 bg-surface-container">
<img class="w-full h-full object-cover transition-transform duration-700 group-hover:scale-105 opacity-90" data-alt="Overhead shot of a clear glass cup of light coffee" src="https://lh3.googleusercontent.com/aida-public/AB6AXuAvPFqdMTW6cTxlJVRFO-qA7X54PexFtreT_8Xwc1WASV24V0glRSxyVaRVnwdZwmAOCrqXorCtKubsIpR6oByNC5cx5gT22YTcWVvVeafF6CYxUhbVvAZUk9bBOIRk5WQGPPUF1LhLTJMnjTxvdFcllqn-CD4bkhXePyTK3c2XdM6g6v5D78MwBTm2v9psZVMFcZ-sAk45ta6-LyAKQP15-cSUgVmbGMSeXnEGrw_f0IZahWotgLzF3WrStt-IHjMTxZP515i-j40"/>
</div>
<blockquote class="font-headline italic text-xl text-on-surface-variant leading-relaxed mb-8 pr-4">
                    "Highly transparent and elegant. It offers a silky mouthfeel with pronounced rose petal aroma and a Meyer lemon sweetness."
                </blockquote>
<div class="mt-auto space-y-6">
<div class="space-y-2">
<div class="flex justify-between items-end">
<span class="font-label text-xs font-semibold text-on-surface">Flavor Match</span>
<span class="font-mono text-sm font-medium text-secondary">84.8%</span>
</div>
<div class="h-0.5 w-full bg-surface-container-high rounded-full overflow-hidden">
<div class="h-full bg-secondary w-[84.8%] transition-all duration-1000"></div>
</div>
</div>
<div class="flex justify-between items-center">
<div class="flex items-center space-x-2 px-3 py-1.5 bg-tertiary/5 rounded-full">
<span class="w-2 h-2 rounded-full bg-tertiary"></span>
<span class="text-xs font-semibold text-tertiary">Low Risk — Consistent, predictable</span>
</div>
<a class="text-xs font-semibold underline underline-offset-4 decoration-outline-variant hover:decoration-secondary transition-colors" href="#">Why this match?</a>
</div>
</div>
</article>
<!-- Result Card 4 -->
<article class="group relative flex flex-col bg-surface-container-lowest rounded-lg p-10 transition-all duration-500 hover:shadow-[0px_12px_32px_rgba(29,28,23,0.06)] hover:ring-1 hover:ring-secondary/30">
<div class="flex justify-between items-start mb-6">
<div class="space-y-1">
<h3 class="font-headline text-3xl text-on-surface leading-tight">Gesha Village</h3>
<p class="font-label text-[10px] uppercase tracking-widest text-on-surface-variant font-bold">Oma Lot • Gardelli Coffee</p>
</div>
<span class="px-3 py-1 bg-surface-container-high text-[10px] font-bold uppercase tracking-wider rounded-full">Light</span>
</div>
<div class="aspect-[4/3] w-full overflow-hidden rounded-lg mb-8 bg-surface-container">
<img class="w-full h-full object-cover transition-transform duration-700 group-hover:scale-105 opacity-90" data-alt="Close up of a barista preparing a Chemex brew" src="https://lh3.googleusercontent.com/aida-public/AB6AXuD0jLKo27DBKRmLU35wHAs2GZAk-rZO7XGJ7kG7Wb2dyZsO4xGh57kYiiRdGPBZoUel33nvjegxNHEYX20JKIAlH4FnZN5t_Kt7uRuDxhoFc2EySLLyeyyU3ock_fbguA5CAfYU_t4RPuDOua5vWUxOWGYRb4uCwg62cn_Bzg2jadw6d0_Ouy6BdeQkuVOaj-sJxwlh7eNeOc2JLsw8aPLVXwmHrLedA-ZsNVQgJSmGXemniEwE3UvWdWZGLWuhMr5qeocCTRNgS7o"/>
</div>
<blockquote class="font-headline italic text-xl text-on-surface-variant leading-relaxed mb-8 pr-4">
                    "An exceptional expression of terroir. Wildflower honey notes combined with complex lemongrass and a vibrant mandarin finish."
                </blockquote>
<div class="mt-auto space-y-6">
<div class="space-y-2">
<div class="flex justify-between items-end">
<span class="font-label text-xs font-semibold text-on-surface">Flavor Match</span>
<span class="font-mono text-sm font-medium text-secondary">95.4%</span>
</div>
<div class="h-0.5 w-full bg-surface-container-high rounded-full overflow-hidden">
<div class="h-full bg-secondary w-[95.4%] transition-all duration-1000"></div>
</div>
</div>
<div class="flex justify-between items-center">
<div class="flex items-center space-x-2 px-3 py-1.5 bg-tertiary/5 rounded-full">
<span class="w-2 h-2 rounded-full bg-tertiary"></span>
<span class="text-xs font-semibold text-tertiary">Low Risk — Consistent, predictable</span>
</div>
<a class="text-xs font-semibold underline underline-offset-4 decoration-outline-variant hover:decoration-secondary transition-colors" href="#">Why this match?</a>
</div>
</div>
</article>
</section>
<!-- Pagination / Load More -->
<div class="flex flex-col items-center pt-16 space-y-4">
<button class="px-12 py-4 bg-primary text-on-primary rounded-full font-bold tracking-wide hover:bg-primary-container hover:text-on-primary-container transition-all shadow-xl shadow-primary/10">
                Explore More Matches
            </button>
<p class="font-label text-xs text-on-surface-variant italic">Showing 4 of 28 curated results for your profile.</p>
</div>
</main>
<!-- Footer Shell -->
<footer class="bg-surface-container-low dark:bg-stone-900 font-label py-12">
<div class="flex flex-col md:flex-row justify-between items-center px-16 w-full max-w-screen-2xl mx-auto space-y-6 md:space-y-0">
<div class="font-sans text-xs uppercase tracking-widest Plus Jakarta Sans text-[#1d1c17]/50 dark:text-stone-500">
                © 2024 Caffe-In Editorial. All Rights Reserved.
            </div>
<div class="flex space-x-12">
<a class="font-sans text-xs uppercase tracking-widest Plus Jakarta Sans text-[#1d1c17]/50 dark:text-stone-500 hover:text-[#6c2f00] dark:hover:text-orange-300 transition-colors" href="#">The Ethos</a>
<a class="font-sans text-xs uppercase tracking-widest Plus Jakarta Sans text-[#1d1c17]/50 dark:text-stone-500 hover:text-[#6c2f00] dark:hover:text-orange-300 transition-colors" href="#">Privacy</a>
<a class="font-sans text-xs uppercase tracking-widest Plus Jakarta Sans text-[#1d1c17]/50 dark:text-stone-500 hover:text-[#6c2f00] dark:hover:text-orange-300 transition-colors" href="#">Contact</a>
</div>
</div>
</footer>
</body></html>

<!-- Caffe-In | Results -->
<!DOCTYPE html>

<html class="light" lang="en"><head>
<meta charset="utf-8"/>
<meta content="width=device-width, initial-scale=1.0" name="viewport"/>
<script src="https://cdn.tailwindcss.com?plugins=forms,container-queries"></script>
<link href="https://fonts.googleapis.com/css2?family=Newsreader:ital,opsz,wght@0,6..72,200..800;1,6..72,200..800&amp;family=Plus+Jakarta+Sans:wght@200..800&amp;family=IBM+Plex+Mono:wght@400;500&amp;display=swap" rel="stylesheet"/>
<link href="https://fonts.googleapis.com/css2?family=Material+Symbols+Outlined:wght@100..700,0..1&amp;display=swap" rel="stylesheet"/>
<link href="https://fonts.googleapis.com/css2?family=Material+Symbols+Outlined:wght,FILL@100..700,0..1&amp;display=swap" rel="stylesheet"/>
<script id="tailwind-config">
      tailwind.config = {
        darkMode: "class",
        theme: {
          extend: {
            colors: {
              "tertiary": "#174a2b",
              "surface-container-high": "#ece8e0",
              "primary-fixed-dim": "#ffb68c",
              "on-tertiary": "#ffffff",
              "inverse-surface": "#32302b",
              "on-primary-container": "#ffc29f",
              "surface": "#fef9f1",
              "surface-container-highest": "#e7e2da",
              "on-secondary": "#ffffff",
              "on-primary": "#ffffff",
              "outline-variant": "#dac2b6",
              "secondary": "#934b00",
              "on-tertiary-fixed": "#00210e",
              "primary": "#6c2f00",
              "on-background": "#1d1c17",
              "on-secondary-fixed": "#301400",
              "on-error-container": "#93000a",
              "surface-container": "#f2ede5",
              "outline": "#877369",
              "on-surface": "#1d1c17",
              "tertiary-fixed-dim": "#9dd3aa",
              "secondary-fixed-dim": "#ffb781",
              "surface-container-lowest": "#ffffff",
              "on-primary-fixed": "#321200",
              "error-container": "#ffdad6",
              "tertiary-container": "#316241",
              "on-error": "#ffffff",
              "secondary-container": "#fea054",
              "inverse-on-surface": "#f5f0e8",
              "primary-fixed": "#ffdbc9",
              "inverse-primary": "#ffb68c",
              "surface-variant": "#e7e2da",
              "secondary-fixed": "#ffdcc5",
              "error": "#ba1a1a",
              "on-secondary-fixed-variant": "#703800",
              "surface-bright": "#fef9f1",
              "surface-tint": "#934b19",
              "on-primary-fixed-variant": "#753401",
              "tertiary-fixed": "#b9efc5",
              "background": "#fef9f1",
              "on-tertiary-fixed-variant": "#1e5031",
              "on-secondary-container": "#703800",
              "surface-dim": "#ded9d2",
              "on-surface-variant": "#54433a",
              "on-tertiary-container": "#a6dcb2",
              "primary-container": "#8b4513",
              "surface-container-low": "#f8f3eb"
            },
            fontFamily: {
              "headline": ["Newsreader", "serif"],
              "body": ["Plus Jakarta Sans", "sans-serif"],
              "label": ["Plus Jakarta Sans", "sans-serif"],
              "mono": ["IBM Plex Mono", "monospace"]
            },
            borderRadius: {"DEFAULT": "1rem", "lg": "2rem", "xl": "3rem", "full": "9999px"},
          },
        },
      }
    </script>
<style>
      .material-symbols-outlined {
        font-variation-settings: 'FILL' 0, 'wght' 400, 'GRAD' 0, 'opsz' 24;
      }
      body {
        background-color: #fef9f1;
        color: #1d1c17;
      }
      .editorial-flow {
        line-height: 1.8;
      }
    </style>
</head>
<body class="font-body selection:bg-primary/10">
<!-- TopNavBar Navigation Shell -->
<nav class="bg-[#fef9f1] dark:bg-stone-950 font-serif text-lg tracking-tight Newsreader docked full-width top-0 sticky z-50 transition-all duration-300">
<div class="flex justify-between items-center w-full px-12 py-6 max-w-screen-2xl mx-auto">
<div class="font-serif italic text-2xl text-[#1d1c17] dark:text-stone-100 flex items-center gap-2">
                Caffe-In
            </div>
<div class="hidden md:flex items-center space-x-12">
<a class="text-[#1d1c17]/60 dark:text-stone-400 font-medium hover:text-[#6c2f00] transition-colors duration-300" href="#">Curations</a>
<a class="text-[#1d1c17]/60 dark:text-stone-400 font-medium hover:text-[#6c2f00] transition-colors duration-300" href="#">Roasters</a>
<a class="text-[#1d1c17]/60 dark:text-stone-400 font-medium hover:text-[#6c2f00] transition-colors duration-300" href="#">Journal</a>
</div>
<div class="flex items-center gap-6">
<span class="material-symbols-outlined text-[#6c2f00] dark:text-orange-200 cursor-pointer">account_circle</span>
</div>
</div>
</nav>
<!-- Main Content Canvas -->
<main class="max-w-screen-xl mx-auto px-6 md:px-16 py-12 md:py-24">
<!-- Hero Header -->
<header class="mb-20">
<div class="flex flex-col md:flex-row md:items-end justify-between gap-8">
<div class="space-y-4 max-w-3xl">
<span class="font-mono text-xs uppercase tracking-[0.2em] text-on-surface-variant/70">Origin: Sidamo region</span>
<h1 class="font-headline text-6xl md:text-8xl font-light leading-none tracking-tight text-on-surface">Ethiopian Yirgacheffe G1</h1>
<div class="flex flex-wrap items-center gap-x-8 gap-y-4 pt-4">
<div class="flex items-center gap-2">
<span class="text-xs font-mono uppercase text-on-surface-variant">Roaster</span>
<span class="text-lg font-medium">Luminous Coffee Co.</span>
</div>
<div class="flex items-center gap-2">
<span class="text-xs font-mono uppercase text-on-surface-variant">Roast Level</span>
<div class="flex gap-1">
<div class="w-3 h-3 rounded-full bg-primary/20"></div>
<div class="w-3 h-3 rounded-full bg-primary/40"></div>
<div class="w-3 h-3 rounded-full bg-primary/10"></div>
</div>
<span class="text-lg font-medium">Light-Medium</span>
</div>
</div>
</div>
<div class="hidden md:block pb-2">
<div class="w-48 h-64 rounded-lg bg-surface-container overflow-hidden">
<img class="w-full h-full object-cover grayscale opacity-80 mix-blend-multiply" data-alt="Close up of roasted coffee beans in a ceramic dish" src="https://lh3.googleusercontent.com/aida-public/AB6AXuABtHzgLsdaMXUWIiHinvojg_swsvTJLrOh8-9DwdRd2D0xJWt7gCvK2eATRiqQjWAAkSxGRfzHRcMJzzsFx7nADGfBMJ8ckiliX01-pBwUDNWOet2vPcoOK1yAqGkgou4uiBwdocOXz_W2xDmAAfPZxUVqfrPUBovpmx9D4BnH9-roNCfKuCLj3hx2Gf84F7k4To8jx-OrfbUxtXd5vOslNtG-TWzrLYSQnALEsgVgv4EqiAZTycCyOU_a2cEgsaNOwjB53QPjFks"/>
</div>
</div>
</div>
</header>
<!-- Section 1: Flavor Profile (Visualized) -->
<section class="mb-24">
<div class="flex flex-col md:flex-row gap-16">
<div class="md:w-1/3">
<h2 class="font-headline text-3xl italic mb-4">Flavor Profile</h2>
<p class="text-on-surface-variant text-sm max-w-xs">A quantitative breakdown of the sensory attributes present in the brew.</p>
</div>
<div class="md:w-2/3 space-y-8">
<div class="space-y-3">
<div class="flex justify-between items-center text-xs font-mono uppercase tracking-widest">
<span>Brightness</span>
<span>85%</span>
</div>
<div class="h-1.5 w-full bg-surface-container-highest rounded-full overflow-hidden">
<div class="h-full bg-secondary-container w-[85%]"></div>
</div>
</div>
<div class="space-y-3">
<div class="flex justify-between items-center text-xs font-mono uppercase tracking-widest">
<span>Body</span>
<span>42%</span>
</div>
<div class="h-1.5 w-full bg-surface-container-highest rounded-full overflow-hidden">
<div class="h-full bg-secondary-container w-[42%]"></div>
</div>
</div>
<div class="space-y-3">
<div class="flex justify-between items-center text-xs font-mono uppercase tracking-widest">
<span>Fruitiness</span>
<span>92%</span>
</div>
<div class="h-1.5 w-full bg-surface-container-highest rounded-full overflow-hidden">
<div class="h-full bg-secondary-container w-[92%]"></div>
</div>
</div>
<div class="space-y-3">
<div class="flex justify-between items-center text-xs font-mono uppercase tracking-widest">
<span>Complexity</span>
<span>78%</span>
</div>
<div class="h-1.5 w-full bg-surface-container-highest rounded-full overflow-hidden">
<div class="h-full bg-secondary-container w-[78%]"></div>
</div>
</div>
</div>
</div>
</section>
<!-- Section 2: Tasting Notes (Editorial) -->
<section class="mb-24 bg-surface-container-low -mx-6 md:-mx-16 px-6 md:px-16 py-20">
<div class="max-w-4xl mx-auto">
<h2 class="font-headline text-3xl italic mb-10 text-center">Tasting Notes</h2>
<div class="editorial-flow font-body text-xl md:text-2xl text-on-surface/90 first-letter:text-7xl first-letter:font-headline first-letter:float-left first-letter:mr-4 first-letter:mt-2">
                    The first sip reveals a shimmering acidity, reminiscent of white peaches and sun-drenched jasmine. As the temperature drops, the profile expands into a complex tapestry of bergamot and honeyed sweetness. There is a tea-like clarity to the body—delicate yet persistent—that finishes with a clean, effervescent linger of lemongrass and Meyer lemon. This is a quintessential heirloom wash, celebrating the precision of high-altitude terroir.
                </div>
<div class="mt-12 flex flex-wrap gap-3 justify-center">
<span class="px-6 py-2 rounded-full bg-surface-container-highest text-sm font-medium">White Peach</span>
<span class="px-6 py-2 rounded-full bg-surface-container-highest text-sm font-medium">Jasmine</span>
<span class="px-6 py-2 rounded-full bg-surface-container-highest text-sm font-medium">Bergamot</span>
<span class="px-6 py-2 rounded-full bg-surface-container-highest text-sm font-medium">Lemongrass</span>
</div>
</div>
</section>
<!-- Section 3: Risk Assessment -->
<section class="mb-24">
<div class="grid grid-cols-1 md:grid-cols-2 gap-16 items-start">
<div class="space-y-8">
<div>
<h2 class="font-headline text-3xl italic mb-6">Risk Assessment</h2>
<div class="inline-flex items-center gap-3 px-4 py-2 rounded-full bg-secondary/5 border border-secondary/10">
<div class="w-2.5 h-2.5 rounded-full bg-secondary animate-pulse"></div>
<span class="text-sm font-semibold text-secondary">Medium Risk — Moderately variable</span>
</div>
</div>
<p class="text-lg text-on-surface-variant editorial-flow">
                        Reviewers had very different experiences with this coffee—expect some unpredictability. While the terroir is exceptional, the delicate light roast requires meticulous extraction control to avoid vegetal undercurrents.
                    </p>
<div class="pt-6">
<div class="text-xs font-mono text-on-surface-variant uppercase mb-2 tracking-tighter">Compatibility Alignment</div>
<div class="text-5xl font-mono text-primary font-light">82% <span class="text-xl">match with your query</span></div>
</div>
</div>
<!-- Abstract Scatter Diagram -->
<div class="bg-surface-container p-12 rounded-lg aspect-square flex flex-col items-center justify-center relative overflow-hidden">
<div class="absolute inset-0 opacity-10 pointer-events-none">
<div class="w-full h-full border-[0.5px] border-on-surface-variant/20 grid grid-cols-8 grid-rows-8"></div>
</div>
<div class="relative w-64 h-64">
<!-- Scatter dots -->
<div class="absolute top-1/4 left-1/3 w-3 h-3 rounded-full bg-secondary/60"></div>
<div class="absolute top-1/2 left-1/4 w-4 h-4 rounded-full bg-secondary"></div>
<div class="absolute top-2/3 left-1/2 w-2 h-2 rounded-full bg-secondary/40"></div>
<div class="absolute top-1/3 right-1/4 w-5 h-5 rounded-full bg-secondary/80"></div>
<div class="absolute bottom-1/4 right-1/3 w-3 h-3 rounded-full bg-secondary/30"></div>
<div class="absolute top-10 right-10 w-2 h-2 rounded-full bg-secondary/50"></div>
<div class="absolute bottom-10 left-10 w-2 h-2 rounded-full bg-secondary/20"></div>
<div class="absolute top-1/2 right-1/2 w-6 h-6 rounded-full bg-secondary/10 border border-secondary/30"></div>
<!-- Connecting lines (abstract) -->
<svg class="absolute inset-0 w-full h-full opacity-20" viewbox="0 0 100 100">
<path class="text-primary" d="M30 25 L40 50 L60 30 L75 70" fill="none" stroke="currentColor"></path>
</svg>
</div>
<div class="mt-8 text-center">
<span class="text-[10px] font-mono uppercase tracking-[0.3em] text-on-surface-variant/60">Flavor Variance Cluster Diagram</span>
</div>
</div>
</div>
</section>
<!-- Navigation Action -->
<footer class="mt-32 pt-12 border-t border-outline-variant/20 text-center">
<a class="inline-flex items-center gap-2 group" href="#">
<span class="material-symbols-outlined text-sm group-hover:-translate-x-1 transition-transform">arrow_back</span>
<span class="font-mono text-xs uppercase tracking-widest text-on-surface/60 group-hover:text-primary transition-colors">Back to results</span>
</a>
</footer>
</main>
<!-- Global Footer -->
<footer class="bg-[#f8f3eb] dark:bg-stone-900 font-sans text-xs uppercase tracking-widest Plus Jakarta Sans full-width py-12 transition-colors duration-500">
<div class="flex flex-col md:flex-row justify-between items-center px-16 w-full max-w-screen-2xl mx-auto gap-8">
<div class="text-[#1d1c17]/50 dark:text-stone-500">
                © 2024 Caffe-In Editorial. All Rights Reserved.
            </div>
<div class="flex gap-12">
<a class="text-[#1d1c17]/50 dark:text-stone-500 hover:text-[#6c2f00] dark:hover:text-orange-300 transition-colors" href="#">The Ethos</a>
<a class="text-[#1d1c17]/50 dark:text-stone-500 hover:text-[#6c2f00] dark:hover:text-orange-300 transition-colors" href="#">Privacy</a>
<a class="text-[#1d1c17]/50 dark:text-stone-500 hover:text-[#6c2f00] dark:hover:text-orange-300 transition-colors" href="#">Contact</a>
</div>
</div>
</footer>
</body></html>

<!-- Caffe-In | Detail View -->
<!DOCTYPE html>

<html class="light" lang="en"><head>
<meta charset="utf-8"/>
<meta content="width=device-width, initial-scale=1.0" name="viewport"/>
<script src="https://cdn.tailwindcss.com?plugins=forms,container-queries"></script>
<link href="https://fonts.googleapis.com/css2?family=Newsreader:ital,opsz,wght@0,6..72,200..800;1,6..72,200..800&amp;family=Plus+Jakarta+Sans:wght@200..800&amp;family=IBM+Plex+Mono:wght@400;500&amp;display=swap" rel="stylesheet"/>
<link href="https://fonts.googleapis.com/css2?family=Material+Symbols+Outlined:wght,FILL@100..700,0..1&amp;display=swap" rel="stylesheet"/>
<link href="https://fonts.googleapis.com/css2?family=Material+Symbols+Outlined:wght,FILL@100..700,0..1&amp;display=swap" rel="stylesheet"/>
<script id="tailwind-config">
      tailwind.config = {
        darkMode: "class",
        theme: {
          extend: {
            colors: {
              "tertiary": "#174a2b",
              "surface-container-high": "#ece8e0",
              "primary-fixed-dim": "#ffb68c",
              "on-tertiary": "#ffffff",
              "inverse-surface": "#32302b",
              "on-primary-container": "#ffc29f",
              "surface": "#fef9f1",
              "surface-container-highest": "#e7e2da",
              "on-secondary": "#ffffff",
              "on-primary": "#ffffff",
              "outline-variant": "#dac2b6",
              "secondary": "#934b00",
              "on-tertiary-fixed": "#00210e",
              "primary": "#6c2f00",
              "on-background": "#1d1c17",
              "on-secondary-fixed": "#301400",
              "on-error-container": "#93000a",
              "surface-container": "#f2ede5",
              "outline": "#877369",
              "on-surface": "#1d1c17",
              "tertiary-fixed-dim": "#9dd3aa",
              "secondary-fixed-dim": "#ffb781",
              "surface-container-lowest": "#ffffff",
              "on-primary-fixed": "#321200",
              "error-container": "#ffdad6",
              "tertiary-container": "#316241",
              "on-error": "#ffffff",
              "secondary-container": "#fea054",
              "inverse-on-surface": "#f5f0e8",
              "primary-fixed": "#ffdbc9",
              "inverse-primary": "#ffb68c",
              "surface-variant": "#e7e2da",
              "secondary-fixed": "#ffdcc5",
              "error": "#ba1a1a",
              "on-secondary-fixed-variant": "#703800",
              "surface-bright": "#fef9f1",
              "surface-tint": "#934b19",
              "on-primary-fixed-variant": "#753401",
              "tertiary-fixed": "#b9efc5",
              "background": "#fef9f1",
              "on-tertiary-fixed-variant": "#1e5031",
              "on-secondary-container": "#703800",
              "surface-dim": "#ded9d2",
              "on-surface-variant": "#54433a",
              "on-tertiary-container": "#a6dcb2",
              "primary-container": "#8b4513",
              "surface-container-low": "#f8f3eb"
            },
            fontFamily: {
              "headline": ["Newsreader", "serif"],
              "body": ["Plus Jakarta Sans", "sans-serif"],
              "label": ["Plus Jakarta Sans", "sans-serif"],
              "mono": ["IBM Plex Mono", "monospace"]
            },
            borderRadius: {"DEFAULT": "1rem", "lg": "2rem", "xl": "3rem", "full": "9999px"},
          },
        },
      }
    </script>
<style>
        body {
            background-color: #fef9f1;
            color: #1d1c17;
            -webkit-font-smoothing: antialiased;
        }
        .material-symbols-outlined {
            font-variation-settings: 'FILL' 0, 'wght' 300, 'GRAD' 0, 'opsz' 24;
        }
    </style>
</head>
<body class="font-body selection:bg-primary-fixed selection:text-on-primary-fixed">
<!-- TopNavBar -->
<nav class="fixed top-0 left-0 right-0 z-50 bg-[#fef9f1]/80 backdrop-blur-xl">
<div class="flex justify-between items-center w-full px-12 py-6 max-w-screen-2xl mx-auto">
<div class="font-serif italic text-2xl text-[#1d1c17] dark:text-stone-100">Caffe-In</div>
<div class="hidden md:flex items-center space-x-12">
<a class="font-serif text-lg tracking-tight Newsreader text-[#1d1c17]/60 hover:text-[#6c2f00] transition-colors duration-300 font-medium" href="#">Curations</a>
<a class="font-serif text-lg tracking-tight Newsreader text-[#1d1c17]/60 hover:text-[#6c2f00] transition-colors duration-300 font-medium" href="#">Roasters</a>
<a class="font-serif text-lg tracking-tight Newsreader text-[#1d1c17]/60 hover:text-[#6c2f00] transition-colors duration-300 font-medium" href="#">Journal</a>
</div>
<div class="flex items-center space-x-6">
<div class="relative hidden sm:block">
<input class="bg-transparent border-b-2 border-outline-variant focus:border-primary transition-colors py-1 outline-none font-label text-sm px-2 w-48" placeholder="Search profiles..." type="text"/>
</div>
<button class="material-symbols-outlined text-on-surface hover:text-primary transition-colors" data-icon="account_circle">account_circle</button>
</div>
</div>
</nav>
<main class="min-h-screen pt-32 pb-24 px-6 flex flex-col items-center justify-center">
<!-- Search Context Header (Asymmetric Layout Element) -->
<div class="w-full max-w-4xl mb-16 flex flex-col md:flex-row items-baseline gap-4 md:gap-12 opacity-40">
<span class="font-mono text-xs uppercase tracking-widest">Search Query</span>
<div class="font-headline italic text-3xl md:text-5xl border-b border-on-surface/20 pb-2 flex-grow">
                "nutty, bright, lavender-infused volcanic honey process"
            </div>
</div>
<!-- Central Editorial Content Container -->
<div class="max-w-xl w-full text-center space-y-10">
<!-- Typographic Illustration -->
<div class="relative inline-block">
<div class="font-headline italic text-[120px] leading-none text-outline-variant/30 select-none">?</div>
<div class="absolute inset-0 flex items-center justify-center">
<div class="w-12 h-[1px] bg-primary/40 rotate-45"></div>
</div>
</div>
<div class="space-y-4">
<h1 class="font-headline text-4xl md:text-5xl text-on-background tracking-tight leading-tight">
                    No matches found for that flavor profile.
                </h1>
<p class="font-body text-lg text-on-surface-variant max-w-md mx-auto leading-relaxed">
                    Try <span class="text-primary italic font-medium">simplifying</span> your description, or swap '<span class="italic">nutty</span>' for '<span class="italic">chocolatey</span>'.
                </p>
</div>
<!-- Suggestion Chips Section -->
<div class="space-y-6 pt-4">
<p class="font-mono text-[10px] uppercase tracking-[0.2em] text-on-surface-variant/60">Alternative Curations</p>
<div class="flex flex-wrap justify-center gap-3">
<button class="px-6 py-3 rounded-full bg-surface-container hover:bg-surface-container-highest transition-all duration-300 text-on-surface font-label text-sm border border-transparent hover:border-outline-variant/30">
                        Nutty dark roast
                    </button>
<button class="px-6 py-3 rounded-full bg-surface-container hover:bg-surface-container-highest transition-all duration-300 text-on-surface font-label text-sm border border-transparent hover:border-outline-variant/30">
                        Berry-forward espresso
                    </button>
<button class="px-6 py-3 rounded-full bg-surface-container hover:bg-surface-container-highest transition-all duration-300 text-on-surface font-label text-sm border border-transparent hover:border-outline-variant/30">
                        Floral tea-like light roast
                    </button>
</div>
</div>
</div>
<!-- Decorative Background Element (Editorial Asymmetry) -->
<div class="fixed bottom-0 right-0 w-1/3 h-1/2 -z-10 pointer-events-none overflow-hidden opacity-50">
<svg class="w-full h-full translate-x-1/4 translate-y-1/4" viewbox="0 0 200 200" xmlns="http://www.w3.org/2000/svg">
<path d="M44.7,-76.4C58.3,-69.2,70.1,-58.3,77.9,-45.3C85.7,-32.3,89.5,-17.1,88.4,-2.5C87.3,12.1,81.4,26.1,72.4,38.2C63.4,50.3,51.3,60.5,38.1,68.4C24.9,76.3,10.7,81.9,-3.2,87.4C-17.1,93,-30.7,98.5,-42.6,94.2C-54.5,89.9,-64.7,75.8,-71.8,61.8C-78.9,47.8,-83,33.9,-84.9,20C-86.8,6.1,-86.5,-7.8,-82.2,-20.5C-77.9,-33.2,-69.6,-44.7,-58.9,-53.2C-48.2,-61.7,-35.1,-67.2,-22.3,-74C-9.5,-80.8,3.1,-88.9,17.4,-86.6C31.7,-84.3,47.7,-71.6,44.7,-76.4Z" fill="#e7e2da" transform="translate(100 100)"></path>
</svg>
</div>
</main>
<!-- Footer -->
<footer class="bg-[#f8f3eb] dark:bg-stone-900 w-full py-12">
<div class="flex flex-col md:flex-row justify-between items-center px-16 w-full max-w-screen-2xl mx-auto space-y-6 md:space-y-0">
<div class="font-sans text-xs uppercase tracking-widest Plus Jakarta Sans text-[#1d1c17]/50 dark:text-stone-500">
                © 2024 Caffe-In Editorial. All Rights Reserved.
            </div>
<div class="flex items-center space-x-12">
<a class="font-sans text-xs uppercase tracking-widest Plus Jakarta Sans text-[#1d1c17]/50 dark:text-stone-500 hover:text-[#6c2f00] dark:hover:text-orange-300 transition-colors" href="#">The Ethos</a>
<a class="font-sans text-xs uppercase tracking-widest Plus Jakarta Sans text-[#1d1c17]/50 dark:text-stone-500 hover:text-[#6c2f00] dark:hover:text-orange-300 transition-colors" href="#">Privacy</a>
<a class="font-sans text-xs uppercase tracking-widest Plus Jakarta Sans text-[#1d1c17]/50 dark:text-stone-500 hover:text-[#6c2f00] dark:hover:text-orange-300 transition-colors" href="#">Contact</a>
</div>
</div>
</footer>
</body></html>