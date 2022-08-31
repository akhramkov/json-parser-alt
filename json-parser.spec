Name: json-parser
Version: 1.1.0
Release: alt1
Summary: Very low footprint JSON parser written in portable ANSI C
License: BSD
Group: Development/C
Url: https://github.com/udp/json-parser
Source0: https://github.com/udp/json-parser/archive/v%version/%name-%version.tar.gz

BuildRequires: gcc

%description
Very low footprint JSON parser written in portable ANSI C

%package devel
Summary: Files needed to develop applications with Very low footprint JSON parser
Group: Development/C
Requires: %name = %version-%release

%description devel
Files needed to develop applications with Very low footprint JSON parser

%prep
%setup -n %name-%version

%build
%configure
%make_build

%install
%makeinstall_std

%files
%doc README.md AUTHORS LICENSE
%_libdir/lib*.so.*

%files devel
%_libdir/lib*.so
%_includedir/%name/
%_datadir/pkgconfig/%name.pc

%changelog
* Wed Aug 31 2022 Andrey Khramkov <aki@altlinux.org> 1.1.0-alt1
- Initial build.

