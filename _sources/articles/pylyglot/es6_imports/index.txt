======================
ES6 Imports with Babel
======================

Overview
========

- Install and configure Babel

- Switch modules and imports from CommonJS to ES6

- Get Babel plugged into frontend toolchain (Mocha, Webpack, ESLint)

Starting Point
==============

- Part webpack, part ESLint, part Mocha

- Ensure ESLint is hooked up in PyCharm

- npm start and npm test, plus Mocha test runner

Installation
============

- npm install --save-dev babel-preset-es2015 babel-loader

Instead of fixing the machinery in advance, we'll make things break, so
you can see how to fix it


ES6 Modules
===========

- Create lib2.js and app2.js (and the places that reference it) and make
  them use ES6

- PyCharm immediately fails...need to set to JavaScript ECMAScript 6

- Make test2.js

- Need to fix .eslintrc

- Mocha run config fails, add .babelrc and change run config and
  package.json to use --compilers js:babel-core/register

- Mocha run config now runs

- webpackconfig module loader, didn't need to configure babel options, as
  they are in .babelrc, point at webpack.config2.js