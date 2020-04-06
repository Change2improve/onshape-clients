/*
 * Onshape REST API
 *
 * The Onshape REST API consumed by all clients.
 *
 * API version: 1.111
 * Contact: api-support@onshape.zendesk.com
 * Generated by: OpenAPI Generator (https://openapi-generator.tech)
 */

package openapi
// BtMaterialLibraryMetadataInfo struct for BtMaterialLibraryMetadataInfo
type BtMaterialLibraryMetadataInfo struct {
	DocumentId string `json:"documentId,omitempty"`
	DocumentName string `json:"documentName,omitempty"`
	ElementId string `json:"elementId,omitempty"`
	IsPublic bool `json:"isPublic,omitempty"`
	LibraryName string `json:"libraryName,omitempty"`
	OwnerName string `json:"ownerName,omitempty"`
	VersionId string `json:"versionId,omitempty"`
	WorkspaceId string `json:"workspaceId,omitempty"`
}