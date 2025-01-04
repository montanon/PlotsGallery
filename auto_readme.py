from pathlib import Path

REPO_URL = "https://github.com/montanon/PlotsGallery/blob/master/plots"
CORE_README = (
    "# PlotsGallery\n"
    + "A gallery to show some plots I've made that I like.\n"
    + "Some of them are made using miPlots (unreleased), others with matplotlib and other libraries.\n\n"
)


def create_readme():
    readme_path = Path(__file__).parent / "README.md"

    plots_paths = list((Path(__file__).parent / "plots").glob("*.png"))
    plots_paths.sort(key=lambda x: int(x.name.split("-")[0]))
    plots = [str(path.name) for path in plots_paths]

    headers = [
        f"## {plot.replace('.png', '').replace('_', ' ').title()}"
        for i, plot in enumerate(plots)
    ]

    with open(readme_path, "w") as f:
        f.write(CORE_README)
        for header, path in zip(headers, plots_paths):
            f.write(f"{header}\n")
            f.write(
                f"![{header.replace('## ', '').split('-')[1]}]({REPO_URL}/{path.name})\n\n"
            )


if __name__ == "__main__":
    create_readme()
