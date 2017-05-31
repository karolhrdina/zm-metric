#
#    zm-metric - agent for getting measurements using LUA and SNMP
#
#    Copyright (C) 2016 - 2017 Tomas Halman                                 
#                                                                           
#    This program is free software; you can redistribute it and/or modify   
#    it under the terms of the GNU General Public License as published by   
#    the Free Software Foundation; either version 2 of the License, or      
#    (at your option) any later version.                                    
#                                                                           
#    This program is distributed in the hope that it will be useful,        
#    but WITHOUT ANY WARRANTY; without even the implied warranty of         
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the          
#    GNU General Public License for more details.                           
#                                                                           
#    You should have received a copy of the GNU General Public License along
#    with this program; if not, write to the Free Software Foundation, Inc.,
#    51 Franklin Street, Fifth Floor, Boston, MA 02110-1301 USA.            
#

# To build with draft APIs, use "--with drafts" in rpmbuild for local builds or add
#   Macros:
#   %_with_drafts 1
# at the BOTTOM of the OBS prjconf
%bcond_with drafts
%if %{with drafts}
%define DRAFTS yes
%else
%define DRAFTS no
%endif
Name:           zm-metric
Version:        1.0.0
Release:        1
Summary:        agent for getting measurements using lua and snmp
License:        MIT
URL:            http://example.com/
Source0:        %{name}-%{version}.tar.gz
Group:          System/Libraries
# Note: ghostscript is required by graphviz which is required by
#       asciidoc. On Fedora 24 the ghostscript dependencies cannot
#       be resolved automatically. Thus add working dependency here!
BuildRequires:  ghostscript
BuildRequires:  asciidoc
BuildRequires:  automake
BuildRequires:  autoconf
BuildRequires:  libtool
BuildRequires:  pkgconfig
BuildRequires:  systemd-devel
BuildRequires:  systemd
%{?systemd_requires}
BuildRequires:  xmlto
BuildRequires:  zeromq-devel
BuildRequires:  czmq-devel
BuildRequires:  malamute-devel
BuildRequires:  zm-proto-devel
BuildRequires:  lua-devel
BuildRequires:  net-snmp-devel
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
zm-metric agent for getting measurements using lua and snmp.

%package -n libzm_metric0
Group:          System/Libraries
Summary:        agent for getting measurements using lua and snmp shared library

%description -n libzm_metric0
This package contains shared library for zm-metric: agent for getting measurements using lua and snmp

%post -n libzm_metric0 -p /sbin/ldconfig
%postun -n libzm_metric0 -p /sbin/ldconfig

%files -n libzm_metric0
%defattr(-,root,root)
%{_libdir}/libzm_metric.so.*

%package devel
Summary:        agent for getting measurements using lua and snmp
Group:          System/Libraries
Requires:       libzm_metric0 = %{version}
Requires:       zeromq-devel
Requires:       czmq-devel
Requires:       malamute-devel
Requires:       zm-proto-devel
Requires:       lua-devel
Requires:       net-snmp-devel

%description devel
agent for getting measurements using lua and snmp development tools
This package contains development files for zm-metric: agent for getting measurements using lua and snmp

%files devel
%defattr(-,root,root)
%{_includedir}/*
%{_libdir}/libzm_metric.so
%{_libdir}/pkgconfig/libzm_metric.pc
%{_mandir}/man3/*
%{_mandir}/man7/*

%prep
%setup -q

%build
sh autogen.sh
%{configure} --enable-drafts=%{DRAFTS} --with-systemd-units
make %{_smp_mflags}

%install
make install DESTDIR=%{buildroot} %{?_smp_mflags}

# remove static libraries
find %{buildroot} -name '*.a' | xargs rm -f
find %{buildroot} -name '*.la' | xargs rm -f

%files
%defattr(-,root,root)
%doc README.md
%{_bindir}/zm-metric
%{_mandir}/man1/zm-metric*
%{_bindir}/zm-metric-rule
%{_mandir}/man1/zm-metric-rule*
%config(noreplace) %{_sysconfdir}/zm-metric/zm-metric.cfg
/usr/lib/systemd/system/zm-metric.service
%dir %{_sysconfdir}/zm-metric
%if 0%{?suse_version} > 1315
%post
%systemd_post zm-metric.service
%preun
%systemd_preun zm-metric.service
%postun
%systemd_postun_with_restart zm-metric.service
%endif

%changelog
