import os
from datetime import datetime

# Define the content template for your Jekyll post
template = """---
layout: post
title: "Automated Report - {date_display}"
date: {date_full}
---
### Status Update for {date_display}
This report was automatically generated at {time_now}.
"""

# Get current timing for filenames and front matter
now = datetime.now()
date_str = now.strftime("%Y-%m-%d")
date_display = now.strftime("%B %d, %Y")
time_now = now.strftime("%H:%M:%S")

# Create the mandatory Jekyll filename: YYYY-MM-DD-title.md
filename = f"_posts/{date_str}-automated-report.md"

# Write the file to the _posts folder
with open(filename, "w") as f:
    f.write(template.format(
        date_display=date_display, 
        date_full=date_str, 
        time_now=time_now
    ))

print(f"Successfully created: {filename}")

