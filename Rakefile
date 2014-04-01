    require 'rubygems'
    require 'rake'
    require 'rdoc'
    require 'date'
    require 'yaml'
    require 'tmpdir'
    require 'jekyll'

    GH_PAGES_DIR= "lony25.github.io"

    desc "Generate blog files"
    task :generate do
      system "jekyll build"
      system "rm -r ../#{GH_PAGES_DIR}/*" unless Dir['../#{GH_PAGES_DIR}/*'].empty?
      system "cp -r _site/* ../#{GH_PAGES_DIR}/"
    end

task :default => :generate