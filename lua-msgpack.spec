%global luaver 5.3
%global lualibdir %{_libdir}/lua/%{luaver}
%global luapkgdir %{_datadir}/lua/%{luaver}
%define debug_package %nil

Name:		lua-msgpack
Version:	0.3.4
Release:	1
Summary:	Parsing Expression Grammars for Lua

Group:		Development/Other
License:	MIT
URL:		http://fperrad.github.io/lua-MessagePack/
Source0:	https://github.com/fperrad/lua-MessagePack/archive/%{version}.tar.gz

BuildRequires:	lua-devel >= %{luaver}
Requires:	lua >= %{luaver}
BuildRequires:	luajit-devel

%description
LPeg is a new pattern-matching library for Lua, based on Parsing Expression
Grammars (PEGs).

%prep
%setup -qn lua-MessagePack-%{version}

%build

%install
mkdir -p %{buildroot}/%{_datadir}/lua/%{luaver}/
cp src5.3/MessagePack.lua %{buildroot}/%{_datadir}/lua/%{luaver}/

%files
%{_datadir}/lua/%{luaver}/MessagePack.lua
