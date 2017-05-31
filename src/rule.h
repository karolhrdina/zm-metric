/*  =========================================================================
    rule - class keeping one JSON rule information

    Copyright (C) 2016 - 2017 Tomas Halman                                 
                                                                           
    This program is free software; you can redistribute it and/or modify   
    it under the terms of the GNU General Public License as published by   
    the Free Software Foundation; either version 2 of the License, or      
    (at your option) any later version.                                    
                                                                           
    This program is distributed in the hope that it will be useful,        
    but WITHOUT ANY WARRANTY; without even the implied warranty of         
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the          
    GNU General Public License for more details.                           
                                                                           
    You should have received a copy of the GNU General Public License along
    with this program; if not, write to the Free Software Foundation, Inc.,
    51 Franklin Street, Fifth Floor, Boston, MA 02110-1301 USA.            
    =========================================================================
*/

#ifndef RULE_H_INCLUDED
#define RULE_H_INCLUDED

#ifdef __cplusplus
extern "C" {
#endif

#ifndef RULE_T_DEFINED
typedef struct _rule_t rule_t;
#define RULE_T_DEFINED
#endif

//  @interface
//  Create a new rule
ZM_METRIC_PRIVATE rule_t *
    rule_new (void);

//  Destroy the rule
ZM_METRIC_PRIVATE void
    rule_destroy (rule_t **self_p);

//  Self test of this class
ZM_METRIC_PRIVATE void
    rule_test (bool verbose);

//  Parse JSON into rule.
ZM_METRIC_PRIVATE int
    rule_parse (rule_t *self, const char *json);

//  Load json rule from file
ZM_METRIC_PRIVATE int
    rule_load (rule_t *self, const char *path);

//  Get the list of assets for which this rule should be applied
ZM_METRIC_PRIVATE zlist_t *
    rule_assets (rule_t *self);

//  Get the list of groups for which this rule should be applied
ZM_METRIC_PRIVATE zlist_t *
    rule_groups (rule_t *self);

//  Get the list of models and PNs for which this rule should be applied
ZM_METRIC_PRIVATE zlist_t *
    rule_models (rule_t *self);

//  Get rule name
ZM_METRIC_PRIVATE const char *
    rule_name (rule_t *self);

//  Get the evaluation function
ZM_METRIC_PRIVATE const char *
    rule_evaluation (rule_t *self);

// rulle polling multiplicator
ZM_METRIC_PRIVATE unsigned int
    rule_polling (rule_t *self);

//  freefn for zhash/zlist
ZM_METRIC_PRIVATE void
    rule_freefn (void *self);
//  @end

ZM_METRIC_PRIVATE void
    vsjson_test (bool verbose);


#ifdef __cplusplus
}
#endif

#endif
