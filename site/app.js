// Injects build metadata at runtime. The CI pipeline rewrites the
// placeholders below using sed before building the Docker image, so the
// deployed page shows the real build number and commit SHA.
(function () {
  const build = "__BUILD_NUMBER__";
  const commit = "__COMMIT_SHA__";

  if (!build.startsWith("__")) {
    document.getElementById("build").textContent = "#" + build;
  }
  if (!commit.startsWith("__")) {
    document.getElementById("commit").textContent = commit.slice(0, 7);
  }
})();
