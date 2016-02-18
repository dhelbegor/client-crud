var gulp = require('gulp'), 
    concat = require('gulp-concat'), 
    minifyCSS = require('gulp-minify-css');
    sass = require('gulp-sass');

var config = {
        styles : 'apps/core/static/sass/main.sass',
};

gulp.task('default',['sass'], function() {

});

gulp.task('sass', function() {

    gulp.src(config.styles)
        .pipe(sass())
        .pipe(minifyCSS())
        .pipe(concat('main.css'))
        .pipe(gulp.dest('apps/core/static/css'));

});
