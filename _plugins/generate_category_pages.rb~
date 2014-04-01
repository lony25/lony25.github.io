class CategoryPages < Generator
  def generate(site)
    site.pages.dup.each do |page|
      paginate(site, page) if CategoryPager.pagination_enabled?(site.config, page)
    end
  end
end
