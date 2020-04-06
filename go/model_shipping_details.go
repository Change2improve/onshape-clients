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
// ShippingDetails struct for ShippingDetails
type ShippingDetails struct {
	Address Address `json:"address,omitempty"`
	Name string `json:"name,omitempty"`
	Phone string `json:"phone,omitempty"`
}