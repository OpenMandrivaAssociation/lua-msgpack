%global luaver 5.3
%global lualibdir %{_libdir}/lua/%{luaver}
%global luapkgdir %{_datadir}/lua/%{luaver}
%define debug_package %nil

Name:		lua-msgpack
Version:	0.5.2
Release:	1
Summary:	Lua implementation of the MessagePack serialization format

Group:		Development/Other
License:	MIT
URL:		https://fperrad.frama.io/lua-MessagePack/
Source0:	https://framagit.org/fperrad/lua-MessagePack/-/archive/%{version}/lua-MessagePack-%{version}.tar.bz2

BuildRequires:	lua-devel >= %{luaver}
Requires:	lua >= %{luaver}
BuildRequires:	luajit-devel

%description
LPeg is a new pattern-matching library for Lua, based on Parsing Expression
Grammars (PEGs).

%prep
%autosetup -p1 -n lua-MessagePack-%{version}

%build

%install
mkdir -p %{buildroot}/%{_datadir}/lua/%{luaver}/
cp src5.3/MessagePack.lua %{buildroot}/%{_datadir}/lua/%{luaver}/

%files
%{_datadir}/lua/%{luaver}/MessagePack.lua
