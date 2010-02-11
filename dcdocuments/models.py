# *-* encoding: utf-8 *-*

## Copyright 2010 Stéphanie Vilayphiou, Alexandre Leray

## This file is part of Django DCDocument.
## 
## Django DCDocument is free software: you can redistribute it and/or modify
## it under the terms of the GNU General Public License as published by
## the Free Software Foundation, either version 3 of the License, or
## any later version.
## 
## Django DCDocument is distributed in the hope that it will be useful,
## but WITHOUT ANY WARRANTY; without even the implied warranty of
## MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
## GNU General Public License for more details.
## 
## You should have received a copy of the GNU General Public License
## along with Django DCDocument.  If not, see <http://www.gnu.org/licenses/>.


from django.db import models
from django.utils.translation import ugettext_lazy as _


class Document(models.Model):
    """
    Meta Class for any document type.
    It implements the Dublin Core Metadata Element Set, Version 1.1.
    See http://dublincore.org/documents/2008/01/14/dces/
    """
    
    help_texts = {
        'contributor' : _('An entity responsible for making contributions to the resource.'),
        'coverage'    : _('The spatial or temporal topic of the resource, the spatial applicability \
                           of the resource, or the jurisdiction under which the resource is relevant.'),
        'creator'     : _('An entity primarily responsible for making the resource.'),
        'date'        : _('A point or period of time associated with an event in the lifecycle of the resource.'),
        'description' : _('An account of the resource.'),
        'format'      : _('The file format, physical medium, or dimensions of the resource.'),
        'identifier'  : _('An unambiguous reference to the resource within a given context.'),
        'language'    : _('A language of the resource.'),
        'publisher'   : _('An entity responsible for making the resource available.'),
        'relation'    : _('A related resource.'),
        'rights'      : _('Information about rights held in and over the resource.'),
        'source'      : _('A related resource from which the described resource is derived.'),
        'subject'     : _('The topic of the resource.'),
        'title'       : _('A name given to the resource.'),
        'type'        : _('The nature or genre of the resource.'),
    }
    
    dc_contributor = models.TextField(blank=True, verbose_name=_('Contributors'), help_text=help_texts['contributor'])
    dc_coverage    = models.TextField(blank=True, verbose_name=_('Coverage'), help_text=help_texts['coverage'])
    dc_creator     = models.TextField(blank=True, verbose_name=_('Creators'), help_text=help_texts['creator'])
    dc_date        = models.TextField(blank=True, verbose_name=_('Date'), help_text=help_texts['date'])
    dc_description = models.TextField(blank=True, verbose_name=_('Description'), help_text=help_texts['description'])
    dc_format      = models.TextField(blank=True, verbose_name=_('Format'), help_text=help_texts['format'])
    dc_identifier  = models.TextField(blank=True, verbose_name=_('Identifier'), help_text=help_texts['identifier'])
    dc_language    = models.TextField(blank=True, verbose_name=_('Language'), help_text=help_texts['language'])
    dc_publisher   = models.TextField(blank=True, verbose_name=_('Publishers'), help_text=help_texts['publisher'])
    dc_relation    = models.TextField(blank=True, verbose_name=_('Relation'), help_text=help_texts['relation'])
    dc_rights      = models.TextField(blank=True, verbose_name=_('Rights'), help_text=help_texts['rights'])
    dc_source      = models.TextField(blank=True, verbose_name=_('Source'), help_text=help_texts['source'])
    dc_subject     = models.TextField(blank=True, verbose_name=_('Subject'), help_text=help_texts['subject'])
    dc_title       = models.TextField(blank=True, verbose_name=_('Title'), help_text=help_texts['title'])
    dc_type        = models.TextField(blank=True, verbose_name=_('Type'), help_text=help_texts['type'])
    
    def __unicode__(self):
        return u'%s' % self.dc_title
    
    class Meta:
        abstract = True

