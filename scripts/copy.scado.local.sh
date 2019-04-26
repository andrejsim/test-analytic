aws s3 ls s3://mg-wst-scado-production-output/GribWriter/v1/Grid/24/20190418T090000Z/ --summarize  --human-readable

aws s3 cp s3://mg-wst-scado-production-output/GribWriter/v1/Grid/24/20190418T090000Z/ ~/data-scado/ --recursive --dryrun --exclude "*" --include "*_TT.grb"