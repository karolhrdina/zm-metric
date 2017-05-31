/*  =========================================================================
    luasnmp - lua snmp extension

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

#ifndef LUASNMP_H_INCLUDED
#define LUASNMP_H_INCLUDED

#include "zm_metric_classes.h"

#ifdef __cplusplus
extern "C" {
#endif

//  @interface
//  Create a new lua state with SNMP support
ZM_METRIC_EXPORT lua_State *
    luasnmp_new (void);

// Destroy luasnmp
ZM_METRIC_EXPORT void
    luasnmp_destroy (lua_State **self_p);

//  Self test of this class
ZM_METRIC_EXPORT void
    luasnmp_test (bool verbose);

//  @end

#ifdef __cplusplus
}
#endif

#endif
