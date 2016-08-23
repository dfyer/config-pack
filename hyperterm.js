module.exports = {
  config: {
    // default font size in pixels for all tabs
    fontSize: 13,

    // font family with optional fallbacks
    fontFamily: 'Menlo, "DejaVu Sans Mono", "Lucida Console", monospace',

    // border color (window, tabs)
    borderColor: '#333',

    // custom css to embed in the main window
    css: '',

    // custom css to embed in the terminal window
    termCSS: '',

    // custom padding (css format, i.e.: `top right bottom left`)
    padding: '12px 14px',

    // terminal cursor background color and opacity (hex, rgb, hsl, hsv, hwb or cmyk)
    cursorColor: 'rgba(248,28,229,0.75)',

    // `BEAM` for |, `UNDERLINE` for _, `BLOCK` for █
    cursorShape: 'BLOCK',

    // Colors
    foregroundColor: '#373b41',
    backgroundColor: '#ffffff',
    colors: {
      black:       '#1d1f21',
      red:         '#cc342b',
      green:       '#198844',
      yellow:      '#fba922',
      blue:        '#3971ed',
      magenta:     '#a36ac7',
      cyan:        '#3971ed',
      white:       '#c5c8c6',
      lightBlack:  '#969896',
      lightRed:    '#cc342b',
      lightGreen:  '#198844',
      lightYellow: '#fba922',
      lightBlue:   '#3971ed',
      lightMagenta:'#a36ac7',
      lightCyan:   '#3971ed',
      lightWhite:  '#ffffff'
    },

    // the shell to run when spawning a new session (i.e. /usr/local/bin/fish)
    // if left empty, your system's login shell will be used by default
    shell: ''

    // for advanced config flags please refer to https://hyperterm.org/#cfg
  },

  // a list of plugins to fetch and install from npm
  // format: [@org/]project[#version]
  // examples:
  //   `hyperpower`
  //   `@company/project`
  //   `project#1.0.1`
  plugins: [],

  // in development, you can create a directory under
  // `~/.hyperterm_plugins/local/` and include it here
  // to load it and avoid it being `npm install`ed
  localPlugins: []
};
