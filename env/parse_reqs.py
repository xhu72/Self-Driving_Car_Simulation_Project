import os

def main():
    with open("package_list (2).txt", "r") as f:
        lines = f.readlines()

    reqs = []
    for line in lines:
        line = line.strip()
        if not line or line.startswith("#"):
            continue
        parts = line.split("=")
        if len(parts) >= 2:
            pkg = parts[0]
            version = parts[1]
            
            # Skip conda and system specific low level packages that pip cannot/should not install
            skip_pkgs = {
                "_tflow_select", "python", "python_abi", "vc", "vs2015_runtime", "ucrt", "mkl", 
                "intel-openmp", "tbb", "libblas", "libcblas", "liblapack", "msys2-conda-epoch", 
                "m2w64-gcc-libs-core", "m2w64-gcc-libs", "m2w64-gmp", "m2w64-libwinpthread-git", 
                "m2w64-gcc-libgfortran", "ca-certificates", "certifi", "openssl", "sqlite", 
                "tk", "zlib", "hdf5", "libprotobuf", "libssh2", "libcurl", "krb5"
            }
            if pkg in skip_pkgs:
                continue
                
            reqs.append(f"{pkg}=={version}")

    with open("requirements.txt", "w") as f:
        f.write("\n".join(reqs) + "\n")
    print("Successfully converted to requirements.txt")

if __name__ == "__main__":
    main()
