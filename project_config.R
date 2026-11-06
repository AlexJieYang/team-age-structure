config_file <- Sys.getenv("PROJECT_CONFIG", unset="config.json")
config <- if (file.exists(config_file)) jsonlite::fromJSON(config_file) else list()
data_default <- if (!is.null(config$data_dir)) config$data_dir else "data"
output_default <- if (!is.null(config$output_dir)) config$output_dir else "outputs"
data_dir <- path.expand(Sys.getenv("PROJECT_DATA_DIR", unset=data_default))
output_dir <- path.expand(Sys.getenv("PROJECT_OUTPUT_DIR", unset=output_default))
table_dir <- file.path(output_dir, "tables")
dir.create(table_dir, recursive=TRUE, showWarnings=FALSE)
input_path <- function(name) {
  path <- file.path(data_dir, name)
  if (!file.exists(path)) stop(paste("Required input:", path, "Set PROJECT_DATA_DIR or data_dir in config.json."))
  path
}
table_path <- function(name) file.path(table_dir, name)
