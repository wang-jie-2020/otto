from pathlib import Path
import re
import json

html_path = Path('D:/Skills/self-fronted-design-attempts/style-recipes-playground.html')
base = Path('D:/Skills/self-fronted-design-attempts/.claude/skills/web-design-engineer/references/style-recipes')

text = html_path.read_text(encoding='utf-8')

index_text = (base / 'INDEX.md').read_text(encoding='utf-8')
mode_map = {}
for mode, label in [('light', 'Light-first'), ('dark', 'Dark-first'), ('either', 'Works either way')]:
    m = re.search(rf'\| {re.escape(label)} \|([^\n]+)', index_text)
    if not m:
        continue
    ids = re.findall(r'\[`([^`]+)`\]\(\./[^\)]+\)', m.group(1))
    for rid in ids:
        mode_map[rid] = mode


def get_section(md: str, start_name: str, end_names: list[str]) -> str:
    start = md.find(f'**{start_name}**')
    if start == -1:
        return ''
    end = len(md)
    for name in end_names:
        idx = md.find(f'**{name}**', start + 1)
        if idx != -1 and idx < end:
            end = idx
    return md[start:end]


def extract_hexes(s: str):
    return re.findall(r'#[0-9A-Fa-f]{3,8}', s)


def normalize_hex(c: str):
    c = c.strip()
    if re.fullmatch(r'#[0-9A-Fa-f]{3}', c):
        return '#' + ''.join(ch * 2 for ch in c[1:]).upper()
    if re.fullmatch(r'#[0-9A-Fa-f]{6}', c):
        return c.upper()
    return c


def rgb_from_hex(c: str):
    c = normalize_hex(c)
    if not re.fullmatch(r'#[0-9A-F]{6}', c):
        return None
    return tuple(int(c[i:i + 2], 16) for i in (1, 3, 5))


def hex_from_rgb(rgb):
    r, g, b = [max(0, min(255, int(round(v)))) for v in rgb]
    return f'#{r:02X}{g:02X}{b:02X}'


def mix(c1: str, c2: str, t: float):
    r1 = rgb_from_hex(c1)
    r2 = rgb_from_hex(c2)
    if not r1 or not r2:
        return c1
    return hex_from_rgb((r1[0] + (r2[0] - r1[0]) * t, r1[1] + (r2[1] - r1[1]) * t, r1[2] + (r2[2] - r1[2]) * t))


def lighten(c: str, t: float):
    return mix(c, '#FFFFFF', t)


def darken(c: str, t: float):
    return mix(c, '#000000', t)


def is_neutral(c: str):
    rgb = rgb_from_hex(c)
    if not rgb:
        return False
    return max(rgb) - min(rgb) < 24


def pick_school_style(school: str):
    if 'Modern Tool' in school:
        return {
            'fonts': {
                'display': "'Inter Tight', 'Inter', 'Noto Sans SC', sans-serif",
                'body': "'Inter', 'Noto Sans SC', sans-serif",
                'ui': "'Inter', 'Noto Sans SC', sans-serif",
                'mono': "'JetBrains Mono', 'SFMono-Regular', Consolas, monospace"
            },
            'metrics': {'displayWeight': 620, 'bodyLine': 1.58, 'labelLetter': '0.12em', 'titleTrack': '-0.02em'},
            'radius': {'sm': 6, 'md': 12, 'lg': 16}
        }
    if 'Editorial / Minimalist' in school:
        return {
            'fonts': {
                'display': "'Noto Serif SC', Georgia, 'Times New Roman', serif",
                'body': "'Noto Serif SC', Georgia, 'Times New Roman', serif",
                'ui': "'IBM Plex Sans', 'Noto Sans SC', sans-serif",
                'mono': "'JetBrains Mono', 'SFMono-Regular', Consolas, monospace"
            },
            'metrics': {'displayWeight': 540, 'bodyLine': 1.66, 'labelLetter': '0.14em', 'titleTrack': '-0.012em'},
            'radius': {'sm': 0, 'md': 0, 'lg': 0}
        }
    if 'Information Architecture' in school:
        return {
            'fonts': {
                'display': "'IBM Plex Sans', 'Helvetica Neue', Arial, sans-serif",
                'body': "'IBM Plex Sans', 'Noto Sans SC', sans-serif",
                'ui': "'IBM Plex Sans', 'Noto Sans SC', sans-serif",
                'mono': "'JetBrains Mono', 'SFMono-Regular', Consolas, monospace"
            },
            'metrics': {'displayWeight': 740, 'bodyLine': 1.5, 'labelLetter': '0.1em', 'titleTrack': '-0.04em'},
            'radius': {'sm': 0, 'md': 0, 'lg': 0}
        }
    if 'Motion / Experimental' in school:
        return {
            'fonts': {
                'display': "'IBM Plex Sans', 'Noto Sans SC', sans-serif",
                'body': "'IBM Plex Sans', 'Noto Sans SC', sans-serif",
                'ui': "'IBM Plex Sans', 'Noto Sans SC', sans-serif",
                'mono': "'JetBrains Mono', 'SFMono-Regular', Consolas, monospace"
            },
            'metrics': {'displayWeight': 700, 'bodyLine': 1.52, 'labelLetter': '0.11em', 'titleTrack': '-0.026em'},
            'radius': {'sm': 4, 'md': 10, 'lg': 14}
        }
    if 'Brutalist / Raw' in school:
        return {
            'fonts': {
                'display': "'IBM Plex Sans', 'Helvetica Neue', Arial, sans-serif",
                'body': "'IBM Plex Sans', 'Noto Sans SC', sans-serif",
                'ui': "'IBM Plex Sans', 'Noto Sans SC', sans-serif",
                'mono': "'JetBrains Mono', 'SFMono-Regular', Consolas, monospace"
            },
            'metrics': {'displayWeight': 770, 'bodyLine': 1.45, 'labelLetter': '0.08em', 'titleTrack': '-0.048em'},
            'radius': {'sm': 0, 'md': 0, 'lg': 0}
        }
    if 'Warm Humanist' in school:
        return {
            'fonts': {
                'display': "'Noto Serif SC', Georgia, 'Times New Roman', serif",
                'body': "'IBM Plex Sans', 'Noto Sans SC', sans-serif",
                'ui': "'IBM Plex Sans', 'Noto Sans SC', sans-serif",
                'mono': "'JetBrains Mono', 'SFMono-Regular', Consolas, monospace"
            },
            'metrics': {'displayWeight': 620, 'bodyLine': 1.62, 'labelLetter': '0.12em', 'titleTrack': '-0.018em'},
            'radius': {'sm': 10, 'md': 16, 'lg': 20}
        }
    return {
        'fonts': {
            'display': "'IBM Plex Sans', 'Noto Sans SC', sans-serif",
            'body': "'IBM Plex Sans', 'Noto Sans SC', sans-serif",
            'ui': "'IBM Plex Sans', 'Noto Sans SC', sans-serif",
            'mono': "'JetBrains Mono', 'SFMono-Regular', Consolas, monospace"
        },
        'metrics': {'displayWeight': 680, 'bodyLine': 1.56, 'labelLetter': '0.11em', 'titleTrack': '-0.022em'},
        'radius': {'sm': 8, 'md': 14, 'lg': 18}
    }


BASE_DARK = {
    '--bg': '#0D1018',
    '--surface1': '#151B27',
    '--surface2': '#1E2636',
    '--surface3': '#2A354A',
    '--line': 'rgba(255,255,255,0.10)',
    '--text-main': '#F4F7FF',
    '--text-sub': '#A8B3CC',
    '--text-muted': '#7D889F',
    '--accent': '#5E6AD2',
    '--accent-ink': '#F7F8FF',
    '--accent-soft': 'rgba(94,106,210,0.24)',
    '--accent-ring': 'rgba(94,106,210,0.34)',
    '--hero-glow': 'rgba(94,106,210,0.30)',
    '--button-bg': '#1E2636',
    '--button-bg-hover': '#2A354A',
    '--button-bg-active': '#34435F',
    '--shadow-elev': '0 18px 50px rgba(0,0,0,0.48)'
}

BASE_LIGHT = {
    '--bg': '#F6F7FB',
    '--surface1': '#FFFFFF',
    '--surface2': '#F0F2F8',
    '--surface3': '#E6EBF4',
    '--line': 'rgba(16,23,41,0.14)',
    '--text-main': '#121829',
    '--text-sub': '#4F5D77',
    '--text-muted': '#74829B',
    '--accent': '#5E6AD2',
    '--accent-ink': '#FFFFFF',
    '--accent-soft': 'rgba(94,106,210,0.18)',
    '--accent-ring': 'rgba(94,106,210,0.24)',
    '--hero-glow': 'rgba(94,106,210,0.20)',
    '--button-bg': '#F0F2F8',
    '--button-bg-hover': '#E6EBF4',
    '--button-bg-active': '#DCE3F0',
    '--shadow-elev': '0 12px 34px rgba(16,22,38,0.15)'
}


def parse_radius(radius_text: str, fallback):
    if not radius_text:
        return dict(fallback)
    low = radius_text.lower()
    nums = [int(n) for n in re.findall(r'\d+', radius_text)]
    if ('none' in low or 'throughout' in low or '0' in low) and all(n <= 2 for n in nums or [0]):
        return {'sm': 0, 'md': 0, 'lg': 0}
    if len(nums) >= 3:
        return {'sm': nums[0], 'md': nums[1], 'lg': nums[2]}
    if len(nums) == 2:
        return {'sm': nums[0], 'md': nums[1], 'lg': nums[1]}
    if len(nums) == 1:
        n = nums[0]
        return {'sm': max(0, n - 4), 'md': n, 'lg': n + 4}
    return dict(fallback)


def build_modes(default_mode: str, mapping: dict, colors: list[str], shadow_text: str):
    def make_default(mode: str):
        pal = dict(BASE_DARK if mode == 'dark' else BASE_LIGHT)
        bg = mapping.get('bg') or (colors[0] if colors else pal['--bg'])
        bg = normalize_hex(bg)
        pal['--bg'] = bg

        if mode == 'dark':
            pal['--surface1'] = normalize_hex(mapping.get('surface1') or (colors[1] if len(colors) > 1 and rgb_from_hex(colors[1]) else lighten(bg, 0.10)))
            pal['--surface2'] = normalize_hex(mapping.get('surface2') or (colors[2] if len(colors) > 2 and rgb_from_hex(colors[2]) else lighten(bg, 0.18)))
            pal['--surface3'] = normalize_hex(mapping.get('surface3') or (colors[3] if len(colors) > 3 and rgb_from_hex(colors[3]) else lighten(bg, 0.26)))
        else:
            pal['--surface1'] = normalize_hex(mapping.get('surface1') or (colors[1] if len(colors) > 1 and rgb_from_hex(colors[1]) else darken(bg, 0.02)))
            pal['--surface2'] = normalize_hex(mapping.get('surface2') or (colors[2] if len(colors) > 2 and rgb_from_hex(colors[2]) else darken(bg, 0.05)))
            pal['--surface3'] = normalize_hex(mapping.get('surface3') or (colors[3] if len(colors) > 3 and rgb_from_hex(colors[3]) else darken(bg, 0.09)))

        accent = mapping.get('accent')
        if not accent:
            for c in colors:
                ch = normalize_hex(c)
                if rgb_from_hex(ch) and not is_neutral(ch):
                    accent = ch
                    break
        if not accent and colors:
            accent = normalize_hex(colors[-1])
        accent = normalize_hex(accent or pal['--accent'])
        pal['--accent'] = accent

        if mapping.get('text_main'):
            pal['--text-main'] = normalize_hex(mapping['text_main'])
        if mapping.get('text_sub'):
            pal['--text-sub'] = normalize_hex(mapping['text_sub'])
        if mapping.get('text_muted'):
            pal['--text-muted'] = normalize_hex(mapping['text_muted'])

        if mapping.get('line'):
            pal['--line'] = mapping['line']

        if mode == 'dark' and pal['--text-main'].startswith('#'):
            rgb = rgb_from_hex(pal['--text-main'])
            if rgb and sum(rgb) < 350:
                pal['--text-main'] = '#F4F7FF'
        if mode == 'light' and pal['--text-main'].startswith('#'):
            rgb = rgb_from_hex(pal['--text-main'])
            if rgb and sum(rgb) > 520:
                pal['--text-main'] = '#121829'

        pal['--accent-ink'] = '#FFFFFF' if mode == 'light' else '#F7F8FF'
        ar, ag, ab = rgb_from_hex(accent) or (94, 106, 210)
        if mode == 'light':
            pal['--accent-soft'] = f'rgba({ar},{ag},{ab},0.16)'
            pal['--accent-ring'] = f'rgba({ar},{ag},{ab},0.24)'
            pal['--hero-glow'] = f'rgba({ar},{ag},{ab},0.18)'
        else:
            pal['--accent-soft'] = f'rgba({ar},{ag},{ab},0.24)'
            pal['--accent-ring'] = f'rgba({ar},{ag},{ab},0.34)'
            pal['--hero-glow'] = f'rgba({ar},{ag},{ab},0.30)'

        pal['--button-bg'] = pal['--surface2']
        pal['--button-bg-hover'] = pal['--surface3']
        pal['--button-bg-active'] = lighten(pal['--surface3'], 0.07) if mode == 'dark' else darken(pal['--surface3'], 0.07)

        if shadow_text and 'none' in shadow_text.lower():
            pal['--shadow-elev'] = 'none'

        return pal

    default_palette = make_default(default_mode)

    if default_mode == 'dark':
        light_palette = dict(BASE_LIGHT)
        bg_l = lighten(default_palette['--bg'], 0.90) if default_palette['--bg'].startswith('#') else BASE_LIGHT['--bg']
        light_palette['--bg'] = bg_l
        light_palette['--surface1'] = darken(bg_l, 0.02)
        light_palette['--surface2'] = darken(bg_l, 0.05)
        light_palette['--surface3'] = darken(bg_l, 0.09)
        light_palette['--accent'] = default_palette['--accent']
        ar, ag, ab = rgb_from_hex(light_palette['--accent']) or (94, 106, 210)
        light_palette['--accent-soft'] = f'rgba({ar},{ag},{ab},0.16)'
        light_palette['--accent-ring'] = f'rgba({ar},{ag},{ab},0.24)'
        light_palette['--hero-glow'] = f'rgba({ar},{ag},{ab},0.18)'
        light_palette['--button-bg'] = light_palette['--surface2']
        light_palette['--button-bg-hover'] = light_palette['--surface3']
        light_palette['--button-bg-active'] = darken(light_palette['--surface3'], 0.07)
        if shadow_text and 'none' in shadow_text.lower():
            light_palette['--shadow-elev'] = 'none'
        return {'dark': default_palette, 'light': light_palette}

    dark_palette = dict(BASE_DARK)
    bg_d = darken(default_palette['--bg'], 0.84) if default_palette['--bg'].startswith('#') else BASE_DARK['--bg']
    dark_palette['--bg'] = bg_d
    dark_palette['--surface1'] = lighten(bg_d, 0.10)
    dark_palette['--surface2'] = lighten(bg_d, 0.18)
    dark_palette['--surface3'] = lighten(bg_d, 0.26)
    dark_palette['--accent'] = default_palette['--accent']
    ar, ag, ab = rgb_from_hex(dark_palette['--accent']) or (94, 106, 210)
    dark_palette['--accent-soft'] = f'rgba({ar},{ag},{ab},0.24)'
    dark_palette['--accent-ring'] = f'rgba({ar},{ag},{ab},0.34)'
    dark_palette['--hero-glow'] = f'rgba({ar},{ag},{ab},0.30)'
    dark_palette['--button-bg'] = dark_palette['--surface2']
    dark_palette['--button-bg-hover'] = dark_palette['--surface3']
    dark_palette['--button-bg-active'] = lighten(dark_palette['--surface3'], 0.07)
    if shadow_text and 'none' in shadow_text.lower():
        dark_palette['--shadow-elev'] = 'none'
    return {'light': default_palette, 'dark': dark_palette}


recipes = {}
for md_path in sorted(base.glob('*.md')):
    if md_path.name == 'INDEX.md':
        continue
    rid = md_path.stem
    md = md_path.read_text(encoding='utf-8')

    title = re.search(r'^#\s+([^\n]+)', md, re.M)
    school = re.search(r'- \*\*School\*\*:\s*(.+)', md)
    vibe = re.search(r'- \*\*Vibe\*\*:\s*(.+)', md)
    best = re.search(r'- \*\*Best for\*\*:\s*(.+)', md)
    spacing = re.search(r'\*\*Spacing\*\*:\s*(.+)', md)
    radius = re.search(r'\*\*Radius\*\*:\s*(.+)', md)
    motion = re.search(r'\*\*Motion\*\*:\s*(.+)', md)
    shadow = re.search(r'\*\*Shadow\*\*:\s*(.+)', md)

    school_text = school.group(1).strip() if school else 'General'
    vibe_text = vibe.group(1).strip() if vibe else 'Distinct design language.'
    best_text = best.group(1).strip() if best else 'General purpose.'

    title_text = title.group(1).strip() if title else rid
    display_name = title_text.split('—', 1)[1].strip() if '—' in title_text else title_text
    short_name = re.sub(r'\s*\(.*?\)', '', display_name).strip()

    palette_section = get_section(md, 'Palette', ['Typography', 'Spacing'])
    signature_section = get_section(md, 'Signature moves', ['Avoid'])
    avoid_section = get_section(md, 'Avoid', ['AI prompt seed', "Don't use when", '---'])

    signature_items = [re.sub(r'^-\s*', '', ln).strip() for ln in signature_section.splitlines() if ln.strip().startswith('- ')]
    avoid_items = [re.sub(r'^-\s*', '', ln).strip() for ln in avoid_section.splitlines() if ln.strip().startswith('- ')]

    colors = []
    for h in extract_hexes(palette_section):
        nh = normalize_hex(h)
        if nh not in colors:
            colors.append(nh)

    mapping = {}
    accent_candidates = []
    line_candidate = None

    for line in palette_section.splitlines():
        raw = line.strip()
        if not raw.startswith('-'):
            continue
        content = raw.lstrip('-').strip()
        label = ''
        value_part = content
        if ':' in content:
            label, value_part = content.split(':', 1)
            label = label.strip().lower()
            value_part = value_part.strip()

        hexes = [normalize_hex(h) for h in extract_hexes(value_part)]
        rgba_match = re.search(r'rgba?\([^\)]+\)', value_part)
        if not hexes and not rgba_match:
            continue

        c = hexes[0] if hexes else None
        if 'ground' in label or 'background' in label:
            if c:
                mapping['bg'] = c
        elif 'surface 1' in label:
            if c:
                mapping['surface1'] = c
        elif 'surface 2' in label:
            if c:
                mapping['surface2'] = c
        elif 'surface 3' in label or 'raised' in label:
            if c:
                mapping['surface3'] = c
        elif 'hairline' in label or 'divider' in label or 'rule' in label:
            if rgba_match:
                line_candidate = rgba_match.group(0)
            elif c:
                line_candidate = c
        elif 'ink' in label or 'primary text' in label or 'high-importance' in label:
            if c:
                mapping['text_main'] = c
        elif 'secondary text' in label:
            if c:
                mapping['text_sub'] = c
        elif 'muted' in label or 'label' in label:
            if c:
                mapping['text_muted'] = c
        elif any(k in label for k in ['accent', 'amber', 'positive', 'negative', 'cobalt', 'brick', 'acid', 'blue', 'red', 'green', 'cyan', 'magenta']):
            accent_candidates.extend(hexes)

    if line_candidate:
        mapping['line'] = line_candidate
    if accent_candidates:
        mapping['accent'] = accent_candidates[0]

    mode_hint = mode_map.get(rid, 'light')
    default_mode = 'dark' if mode_hint == 'dark' else 'light'

    style = pick_school_style(school_text)
    radius_values = parse_radius(radius.group(1).strip() if radius else '', style['radius'])
    modes = build_modes(default_mode, mapping, colors, shadow.group(1).strip() if shadow else '')

    hero_title = short_name if len(short_name) <= 34 else short_name[:31] + '...'
    hero_copy = f"{vibe_text} 适合：{best_text}"

    recipes[rid] = {
        'name': short_name,
        'school': school_text,
        'vibe': vibe_text,
        'bestFor': best_text,
        'defaultMode': default_mode,
        'heroTitle': hero_title,
        'heroCopy': hero_copy,
        'ctaPrimary': 'Apply recipe',
        'ctaSecondary': 'View tokens',
        'signature': signature_items[:4] if signature_items else ['遵循该 recipe 的核心特征。'],
        'avoid': avoid_items[:4] if avoid_items else ['避免偏离 recipe 的视觉语言。'],
        'spacing': spacing.group(1).strip() if spacing else 'follow recipe',
        'motion': motion.group(1).strip() if motion else 'follow recipe',
        'fonts': style['fonts'],
        'metrics': style['metrics'],
        'radius': radius_values,
        'modes': modes
    }

# Keep custom copy for three manually tuned recipes
if 'linear' in recipes:
    recipes['linear']['heroTitle'] = 'Build fast. Stay precise.'
    recipes['linear']['heroCopy'] = '同一结构，不同 token。切换配色和排版后，语气会从“理性克制”到“柔和人文”再到“强势宣言”明显变化。'
    recipes['linear']['ctaPrimary'] = 'Request access'
    recipes['linear']['ctaSecondary'] = 'View demo'
if 'aesop' in recipes:
    recipes['aesop']['heroTitle'] = 'Ritual before speed.'
    recipes['aesop']['heroCopy'] = 'Aesop 语气强调“慢阅读”与材质感：更长行文、低对比层级、几乎无阴影。视觉重心在文字节奏。'
    recipes['aesop']['ctaPrimary'] = 'Explore ritual'
    recipes['aesop']['ctaSecondary'] = 'Ingredients'
if 'pentagram' in recipes:
    recipes['pentagram']['heroTitle'] = 'Make type do the work.'
    recipes['pentagram']['heroCopy'] = 'Pentagram 路线把视觉权重交给字重、尺度和网格。图形退后，信息结构站到前排。'
    recipes['pentagram']['ctaPrimary'] = 'Open brief'
    recipes['pentagram']['ctaSecondary'] = 'Grid spec'

text = re.sub(
    r'(<label for="recipeSelect">Recipe</label>\s*<select id="recipeSelect">)([\s\S]*?)(\s*</select>)',
    r'\1\3',
    text,
    count=1
)

recipes_js = 'const recipes = ' + json.dumps(recipes, ensure_ascii=False, indent=6) + ';'
text, count = re.subn(
    r'const recipes = \{[\s\S]*?\n    \};\n\n    const tokenOrder =',
    recipes_js + '\n\n    const tokenOrder =',
    text,
    count=1
)
if count != 1:
    raise RuntimeError('Failed to replace recipes object')

old_block = """function renderList(node, items) {
      node.innerHTML = items.map((item) => `<li>${item}</li>`).join('');
    }

    function applyRecipe() {
"""

new_block = """function renderList(node, items) {
      node.innerHTML = items.map((item) => `<li>${item}</li>`).join('');
    }

    function schoolSortKey(school) {
      const order = [
        'Modern Tool / Builder SaaS',
        'Editorial / Minimalist',
        'Information Architecture',
        'Motion / Experimental',
        'Brutalist / Raw',
        'Warm Humanist',
        'Specialty / Genre'
      ];
      const hit = order.findIndex((prefix) => school.startsWith(prefix));
      return hit === -1 ? order.length : hit;
    }

    function populateRecipeSelect() {
      const entries = Object.entries(recipes).sort((a, b) => {
        const schoolDiff = schoolSortKey(a[1].school) - schoolSortKey(b[1].school);
        if (schoolDiff !== 0) return schoolDiff;
        return a[1].name.localeCompare(b[1].name, 'zh-Hans-CN');
      });

      const groups = new Map();
      for (const [key, recipe] of entries) {
        if (!groups.has(recipe.school)) {
          groups.set(recipe.school, []);
        }
        groups.get(recipe.school).push([key, recipe]);
      }

      recipeSelect.innerHTML = '';

      for (const [school, list] of groups.entries()) {
        const optgroup = document.createElement('optgroup');
        optgroup.label = school;

        for (const [key, recipe] of list) {
          const option = document.createElement('option');
          option.value = key;
          option.textContent = recipe.name;
          optgroup.appendChild(option);
        }

        recipeSelect.appendChild(optgroup);
      }
    }

    function applyRecipe() {
"""

if old_block not in text:
    raise RuntimeError('Failed to locate renderList/applyRecipe block')
text = text.replace(old_block, new_block, 1)

text = text.replace(
"""      const key = recipeSelect.value;
      const recipe = recipes[key];
      const chosenMode = modeSelect.value === 'recipe' ? recipe.defaultMode : modeSelect.value;
      const palette = recipe.modes[chosenMode];

      document.body.dataset.mode = chosenMode;
""",
"""      const key = recipeSelect.value;
      const recipe = recipes[key];
      if (!recipe) return;

      const requestedMode = modeSelect.value === 'recipe' ? recipe.defaultMode : modeSelect.value;
      const chosenMode = recipe.modes[requestedMode]
        ? requestedMode
        : recipe.modes[recipe.defaultMode]
          ? recipe.defaultMode
          : Object.keys(recipe.modes)[0];
      const palette = recipe.modes[chosenMode];

      document.body.dataset.mode = chosenMode;
""",
1
)

text = text.replace(
"""    recipeSelect.addEventListener('change', applyRecipe);
    modeSelect.addEventListener('change', applyRecipe);
    densitySelect.addEventListener('change', applyRecipe);

    applyRecipe();
""",
"""    recipeSelect.addEventListener('change', applyRecipe);
    modeSelect.addEventListener('change', applyRecipe);
    densitySelect.addEventListener('change', applyRecipe);

    populateRecipeSelect();
    recipeSelect.value = recipes.linear ? 'linear' : Object.keys(recipes)[0];
    applyRecipe();
""",
1
)

html_path.write_text(text, encoding='utf-8')
print(f'Updated {html_path}')
print(f'Recipes loaded: {len(recipes)}')
