%global tag d63011e

Name:           sisu-maven-plugin
Version:        1.1
Release:        7%{?dist}
Summary:        Sisu plugin for Apache Maven
BuildArch:      noarch
Group:          Development/Tools
License:        ASL 2.0 or EPL
URL:            http://sonatype.github.com/%{name}/
Source:         https://github.com/sonatype/%{name}/tarball/%{name}-%{version}#/%{name}-%{version}.tar.gz

BuildRequires:  maven-local
BuildRequires:  java-devel
BuildRequires:  maven-common-artifact-filters
BuildRequires:  plexus-utils
BuildRequires:  sisu
BuildRequires:  sonatype-plugins-parent
# test deps
BuildRequires:  junit
BuildRequires:  maven-surefire-provider-junit4


%description
The Sisu Plugin for Maven provides mojos to generate
META-INF/sisu/javax.inject.Named index files for the Sisu container.

%package        javadoc
Summary:        API documentation for %{name}
Group:          Documentation

%description    javadoc
This package provides %{summary}.

%prep
%setup -q -n sonatype-%{name}-%{tag}

%build
%mvn_file  : %{name}
%mvn_build

%install
%mvn_install

%files -f .mfiles
%doc LICENSE-ASL.txt LICENSE-EPL.txt README.md

%files javadoc -f .mfiles-javadoc
%doc LICENSE-ASL.txt LICENSE-EPL.txt


%changelog
* Fri Jun 28 2013 Mikolaj Izdebski <mizdebsk@redhat.com> - 1.1-7
- Rebuild to regenerate API documentation
- Resolves: CVE-2013-1571

* Mon May 27 2013 Mikolaj Izdebski <mizdebsk@redhat.com> - 1.1-6
- Fix license tag

* Fri Feb 15 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Wed Feb 06 2013 Java SIG <java-devel@lists.fedoraproject.org> - 1.1-4
- Update for https://fedoraproject.org/wiki/Fedora_19_Maven_Rebuild
- Replace maven BuildRequires with maven-local

* Wed Jan 16 2013 Michal Srb <msrb@redhat.com> - 1.1-3
- Build with xmvn

* Wed Aug  8 2012 Mikolaj Izdebski <mizdebsk@redhat.com> - 1.1-2
- Added parent POM dependency

* Tue Jul 24 2012 Mikolaj Izdebski <mizdebsk@redhat.com> - 1.1-1
- Initial packaging
