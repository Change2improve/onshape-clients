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

import { BTMetadataPropertyInfo } from './bTMetadataPropertyInfo';
import { BTReleasePackageItemError } from './bTReleasePackageItemError';

export class BTReleasePackageItemInfo {
    'properties'?: Array<BTMetadataPropertyInfo>;
    'mimeType'?: string;
    'workspaceId'?: string;
    'partId'?: string;
    'elementType'?: number;
    'configuration'?: string;
    'errors'?: Array<BTReleasePackageItemError>;
    'configurationKey'?: string;
    'versionId'?: string;
    'documentId'?: string;
    'companyId'?: string;
    'elementId'?: string;
    'diffThumbnailConfigurationKey'?: string;
    'isIncludedEditable'?: boolean;
    'smallThumbnailHref'?: string;
    'isRevisionManaged'?: boolean;
    'rpid'?: string;
    'obsoletionRevisionId'?: string;
    'name'?: string;
    'id'?: string;
    'href'?: string;
    'viewRef'?: string;

    static discriminator: string | undefined = undefined;

    static attributeTypeMap: Array<{name: string, baseName: string, type: string}> = [
        {
            "name": "properties",
            "baseName": "properties",
            "type": "Array<BTMetadataPropertyInfo>"
        },
        {
            "name": "mimeType",
            "baseName": "mimeType",
            "type": "string"
        },
        {
            "name": "workspaceId",
            "baseName": "workspaceId",
            "type": "string"
        },
        {
            "name": "partId",
            "baseName": "partId",
            "type": "string"
        },
        {
            "name": "elementType",
            "baseName": "elementType",
            "type": "number"
        },
        {
            "name": "configuration",
            "baseName": "configuration",
            "type": "string"
        },
        {
            "name": "errors",
            "baseName": "errors",
            "type": "Array<BTReleasePackageItemError>"
        },
        {
            "name": "configurationKey",
            "baseName": "configurationKey",
            "type": "string"
        },
        {
            "name": "versionId",
            "baseName": "versionId",
            "type": "string"
        },
        {
            "name": "documentId",
            "baseName": "documentId",
            "type": "string"
        },
        {
            "name": "companyId",
            "baseName": "companyId",
            "type": "string"
        },
        {
            "name": "elementId",
            "baseName": "elementId",
            "type": "string"
        },
        {
            "name": "diffThumbnailConfigurationKey",
            "baseName": "diffThumbnailConfigurationKey",
            "type": "string"
        },
        {
            "name": "isIncludedEditable",
            "baseName": "isIncludedEditable",
            "type": "boolean"
        },
        {
            "name": "smallThumbnailHref",
            "baseName": "smallThumbnailHref",
            "type": "string"
        },
        {
            "name": "isRevisionManaged",
            "baseName": "isRevisionManaged",
            "type": "boolean"
        },
        {
            "name": "rpid",
            "baseName": "rpid",
            "type": "string"
        },
        {
            "name": "obsoletionRevisionId",
            "baseName": "obsoletionRevisionId",
            "type": "string"
        },
        {
            "name": "name",
            "baseName": "name",
            "type": "string"
        },
        {
            "name": "id",
            "baseName": "id",
            "type": "string"
        },
        {
            "name": "href",
            "baseName": "href",
            "type": "string"
        },
        {
            "name": "viewRef",
            "baseName": "viewRef",
            "type": "string"
        }    ];

    static getAttributeTypeMap() {
        return BTReleasePackageItemInfo.attributeTypeMap;
    }
}

