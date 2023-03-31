%bcond_without check
%global debug_package %{nil}

%global crate semver

Name:           rust-%{crate}
Version:        1.0.4
Release:        2
Summary:        Parser and evaluator for Cargo's flavor of Semantic Versioning

# Upstream license specification: MIT OR Apache-2.0
License:        MIT OR Apache-2.0
URL:            https://crates.io/crates/semver
Source:         %{crates_source}

ExclusiveArch:  %{rust_arches}
%if %{__cargo_skip_build}
BuildArch:      noarch
%endif

BuildRequires:  rust-packaging

%global _description %{expand:
Parser and evaluator for Cargo's flavor of Semantic Versioning.}

%description %{_description}

%package        devel
Summary:        %{summary}
BuildArch:      noarch
Provides:       crate(semver) = 1.0.4
Requires:       cargo

%description    devel %{_description}

This package contains library source intended for building other packages
which use "%{crate}" crate.

%files          devel
%license LICENSE-MIT LICENSE-APACHE
%doc README.md
%{cargo_registry}/%{crate}-%{version_no_tilde}/

%package     -n %{name}+default-devel
Summary:        %{summary}
BuildArch:      noarch
Provides:       crate(semver/default) = 1.0.4
Requires:       cargo
Requires:       crate(semver) = 1.0.4
Requires:       crate(semver/std) = 1.0.4

%description -n %{name}+default-devel %{_description}

This package contains library source intended for building other packages
which use "default" feature of "%{crate}" crate.

%files       -n %{name}+default-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+serde-devel
Summary:        %{summary}
BuildArch:      noarch
Provides:       crate(semver/serde) = 1.0.4
Requires:       cargo
Requires:       (crate(serde) >= 1.0.0 with crate(serde) < 2.0.0)
Requires:       crate(semver) = 1.0.4

%description -n %{name}+serde-devel %{_description}

This package contains library source intended for building other packages
which use "serde" feature of "%{crate}" crate.

%files       -n %{name}+serde-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+std-devel
Summary:        %{summary}
BuildArch:      noarch
Provides:       crate(semver/std) = 1.0.4
Requires:       cargo
Requires:       crate(semver) = 1.0.4

%description -n %{name}+std-devel %{_description}

This package contains library source intended for building other packages
which use "std" feature of "%{crate}" crate.

%files       -n %{name}+std-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%prep
%autosetup -n %{crate}-%{version_no_tilde} -p1
%cargo_prep

%build
%cargo_build

%install
%cargo_install

%if %{with check}
%check
%cargo_test
%endif
