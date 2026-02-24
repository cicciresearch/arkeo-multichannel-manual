import os

# This function generates the tabs containing sample holder PCBs. 
# It is called by /hardware/sample-holder/sampleholder.md
def define_env(env):

    @env.macro
    def gallery_by_category(page):
        docs_dir = env.conf['docs_dir']
        base_folder = os.path.dirname(page.file.src_path)
        full_base_path = os.path.join(docs_dir, base_folder)

        if not os.path.exists(full_base_path):
            return "<p>Folder not found.</p>"

        # Get subfolders (categories)
        categories = sorted([
            d for d in os.listdir(full_base_path)
            if os.path.isdir(os.path.join(full_base_path, d))
        ])

        if not categories:
            return "<p>No categories found.</p>"

        md = ""

        for category in categories:
            md += f'=== "{category}"\n\n'

            category_path = os.path.join(full_base_path, category)

            images = sorted([
                f for f in os.listdir(category_path)
                if f.lower().endswith((".png", ".jpg", ".jpeg", ".webp"))
            ])

            for img in images:
                name = os.path.splitext(img)[0]
                md += f'    === "{name}"\n\n'
                md += f'        ![{name}]({category}/{img})\n\n'

        return md
