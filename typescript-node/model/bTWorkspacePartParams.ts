/**
 * Onshape REST API
 * The Onshape REST API consumed by all clients.
 *
 * OpenAPI spec version: 1.93
 * Contact: api-support@onshape.zendesk.com
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

import { BTCustomPropertyDefinitionParams } from './bTCustomPropertyDefinitionParams';
import { BTMaterialParams } from './bTMaterialParams';
import { BTNameValuePair } from './bTNameValuePair';
import { BTPartAppearanceParams } from './bTPartAppearanceParams';

export class BTWorkspacePartParams {
    'name'?: string;
    'description'?: string;
    'revision'?: string;
    'customProperties'?: Array<BTNameValuePair>;
    'vendor'?: string;
    'productLine'?: string;
    'title1'?: string;
    'title2'?: string;
    'title3'?: string;
    'partId'?: string;
    'configuration'?: string;
    'elementId'?: string;
    'project'?: string;
    'connectionId'?: string;
    'material'?: BTMaterialParams;
    'partNumber'?: string;
    'appearance'?: BTPartAppearanceParams;
    'customPropertyDefinitions'?: Array<BTCustomPropertyDefinitionParams>;
    'applyUpdateToAllConfigurations'?: boolean;

    static discriminator: string | undefined = undefined;

    static attributeTypeMap: Array<{name: string, baseName: string, type: string}> = [
        {
            "name": "name",
            "baseName": "name",
            "type": "string"
        },
        {
            "name": "description",
            "baseName": "description",
            "type": "string"
        },
        {
            "name": "revision",
            "baseName": "revision",
            "type": "string"
        },
        {
            "name": "customProperties",
            "baseName": "customProperties",
            "type": "Array<BTNameValuePair>"
        },
        {
            "name": "vendor",
            "baseName": "vendor",
            "type": "string"
        },
        {
            "name": "productLine",
            "baseName": "productLine",
            "type": "string"
        },
        {
            "name": "title1",
            "baseName": "title1",
            "type": "string"
        },
        {
            "name": "title2",
            "baseName": "title2",
            "type": "string"
        },
        {
            "name": "title3",
            "baseName": "title3",
            "type": "string"
        },
        {
            "name": "partId",
            "baseName": "partId",
            "type": "string"
        },
        {
            "name": "configuration",
            "baseName": "configuration",
            "type": "string"
        },
        {
            "name": "elementId",
            "baseName": "elementId",
            "type": "string"
        },
        {
            "name": "project",
            "baseName": "project",
            "type": "string"
        },
        {
            "name": "connectionId",
            "baseName": "connectionId",
            "type": "string"
        },
        {
            "name": "material",
            "baseName": "material",
            "type": "BTMaterialParams"
        },
        {
            "name": "partNumber",
            "baseName": "partNumber",
            "type": "string"
        },
        {
            "name": "appearance",
            "baseName": "appearance",
            "type": "BTPartAppearanceParams"
        },
        {
            "name": "customPropertyDefinitions",
            "baseName": "customPropertyDefinitions",
            "type": "Array<BTCustomPropertyDefinitionParams>"
        },
        {
            "name": "applyUpdateToAllConfigurations",
            "baseName": "applyUpdateToAllConfigurations",
            "type": "boolean"
        }    ];

    static getAttributeTypeMap() {
        return BTWorkspacePartParams.attributeTypeMap;
    }
}

