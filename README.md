Site build using Quarto project.

##For future me
To reach the original source, checkout source branch.
Make sure quarto is installed on the system.
Clone the repository

Important information.
Site is published from gh-pages.
When blog is ready, add it to posts or tech (or any future category) folder.
Follow this structure:
posts/YYYY/MM/DD/<url name of file>.md

To publish the post, run following command (ensure git push is available)
quarto publish gh-pages

To create new category:
create folder with category name (for example tech)
create category name.qmd (copy from the other one and make relevant changes)
in the folder, add _metadata.yml (common points that should apply to all posts in that category)

In _quarto.yml, add details in navbar section for that category.

If folder starts with "_", it won't get rendered, so all drafts posts stay in "_draft" section. 

For more details on quarto, visit: https://quarto.org/
