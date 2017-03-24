
package us.kbase.readsapi;

import java.util.HashMap;
import java.util.Map;
import javax.annotation.Generated;
import com.fasterxml.jackson.annotation.JsonAnyGetter;
import com.fasterxml.jackson.annotation.JsonAnySetter;
import com.fasterxml.jackson.annotation.JsonInclude;
import com.fasterxml.jackson.annotation.JsonProperty;
import com.fasterxml.jackson.annotation.JsonPropertyOrder;


/**
 * <p>Original spec-file type: ReadsParams</p>
 * <pre>
 * ReadsAPI parameters
 *        string id - id of object
 *        string name - name of object
 *        string workspace_name - name of workspace
 *        string workspace_id - id of workspace
 *        string string workspace_obj_ref - workspace object ref
 * </pre>
 * 
 */
@JsonInclude(JsonInclude.Include.NON_NULL)
@Generated("com.googlecode.jsonschema2pojo")
@JsonPropertyOrder({
    "id",
    "name",
    "workspace_name",
    "workspace_id",
    "workspace_obj_ref"
})
public class ReadsParams {

    @JsonProperty("id")
    private String id;
    @JsonProperty("name")
    private String name;
    @JsonProperty("workspace_name")
    private String workspaceName;
    @JsonProperty("workspace_id")
    private String workspaceId;
    @JsonProperty("workspace_obj_ref")
    private String workspaceObjRef;
    private Map<String, Object> additionalProperties = new HashMap<String, Object>();

    @JsonProperty("id")
    public String getId() {
        return id;
    }

    @JsonProperty("id")
    public void setId(String id) {
        this.id = id;
    }

    public ReadsParams withId(String id) {
        this.id = id;
        return this;
    }

    @JsonProperty("name")
    public String getName() {
        return name;
    }

    @JsonProperty("name")
    public void setName(String name) {
        this.name = name;
    }

    public ReadsParams withName(String name) {
        this.name = name;
        return this;
    }

    @JsonProperty("workspace_name")
    public String getWorkspaceName() {
        return workspaceName;
    }

    @JsonProperty("workspace_name")
    public void setWorkspaceName(String workspaceName) {
        this.workspaceName = workspaceName;
    }

    public ReadsParams withWorkspaceName(String workspaceName) {
        this.workspaceName = workspaceName;
        return this;
    }

    @JsonProperty("workspace_id")
    public String getWorkspaceId() {
        return workspaceId;
    }

    @JsonProperty("workspace_id")
    public void setWorkspaceId(String workspaceId) {
        this.workspaceId = workspaceId;
    }

    public ReadsParams withWorkspaceId(String workspaceId) {
        this.workspaceId = workspaceId;
        return this;
    }

    @JsonProperty("workspace_obj_ref")
    public String getWorkspaceObjRef() {
        return workspaceObjRef;
    }

    @JsonProperty("workspace_obj_ref")
    public void setWorkspaceObjRef(String workspaceObjRef) {
        this.workspaceObjRef = workspaceObjRef;
    }

    public ReadsParams withWorkspaceObjRef(String workspaceObjRef) {
        this.workspaceObjRef = workspaceObjRef;
        return this;
    }

    @JsonAnyGetter
    public Map<String, Object> getAdditionalProperties() {
        return this.additionalProperties;
    }

    @JsonAnySetter
    public void setAdditionalProperties(String name, Object value) {
        this.additionalProperties.put(name, value);
    }

    @Override
    public String toString() {
        return ((((((((((((("ReadsParams"+" [id=")+ id)+", name=")+ name)+", workspaceName=")+ workspaceName)+", workspaceId=")+ workspaceId)+", workspaceObjRef=")+ workspaceObjRef)+", additionalProperties=")+ additionalProperties)+"]");
    }

}
