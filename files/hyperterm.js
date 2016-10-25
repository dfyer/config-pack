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
    foregroundColor: '#d3d0c8',
    backgroundColor: '#2d2d2d',
    colors: {
      black:       '#2d2d2d',
      red:         '#f2777a',
      green:       '#99cc99',
      yellow:      '#ffcc66',
      blue:        '#6699cc',
      magenta:     '#cc99cc',
      cyan:        '#66cccc',
      white:       '#d3d0c8',
      lightBlack:  '#747369',
      lightRed:    '#f2777a',
      lightGreen:  '#99cc99',
      lightYellow: '#ffcc66',
      lightBlue:   '#6699cc',
      lightMagenta:'#cc99cc',
      lightCyan:   '#66cccc',
      lightWhite:  '#f2f0ec'
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
  plugins: ['hyperline'],

  // in development, you can create a directory under
  // `~/.hyperterm_plugins/local/` and include it here
  // to load it and avoid it being `npm install`ed
  localPlugins: []
};
