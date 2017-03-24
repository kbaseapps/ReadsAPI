
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
 * <p>Original spec-file type: ReadsInfoAll</p>
 * <pre>
 * Reads info all
 *         string id
 *         string Name;
 *         string workspace_name
 *         string Type
 *         string Platform
 *         string Single_Genome
 *         string Strain
 *         string Source
 *         string Number_of_Reads
 *         string Total_Number_of_Bases
 *         string GC_Percentage
 *         string Mean_Read_Length
 *         string Read_Length_Std_Dev
 *         string Phred_Type
 *         string Number_of_Duplicate_Reads - number of duplicate and (%)
 *         string Quality_Score_Min_Max - quality min and max X/ Y
 *         string Quality_Score_Mean_Std_Dev - mean (st dev)
 *         string Insert_Size_Mean
 *         string Insert_Size_Std_Dev
 *         string Outward_Read_Orientation
 *         string Base_Percentages - A (%), C(%), G (%), T (%), N (%)
 *         @optional Single_Genome Strain Source Number_of_Reads Total_Number_of_Bases GC_Percentage
 *         @optional Mean_Read_Length Read_Length_Std_Dev Phred_Type Number_of_Duplicate_Reads
 *         @optional Quality_Score_Min_Max Quality_Score_Mean_Std_Dev
 *         @optional Insert_Size_Mean Insert_Size_Std_Dev Outward_Read_Orientation Base_Percentages
 * </pre>
 * 
 */
@JsonInclude(JsonInclude.Include.NON_NULL)
@Generated("com.googlecode.jsonschema2pojo")
@JsonPropertyOrder({
    "id",
    "Name",
    "workspace_name",
    "Type",
    "Platform",
    "Single_Genome",
    "Strain",
    "Source",
    "Number_of_Reads",
    "Total_Number_of_Bases",
    "GC_Percentage",
    "Mean_Read_Length",
    "Read_Length_Std_Dev",
    "Phred_Type",
    "Number_of_Duplicate_Reads",
    "Quality_Score_Min_Max",
    "Quality_Score_Mean_Std_Dev",
    "Insert_Size_Mean",
    "Insert_Size_Std_Dev",
    "Outward_Read_Orientation",
    "Base_Percentages"
})
public class ReadsInfoAll {

    @JsonProperty("id")
    private String id;
    @JsonProperty("Name")
    private String Name;
    @JsonProperty("workspace_name")
    private String workspaceName;
    @JsonProperty("Type")
    private String Type;
    @JsonProperty("Platform")
    private String Platform;
    @JsonProperty("Single_Genome")
    private String SingleGenome;
    @JsonProperty("Strain")
    private String Strain;
    @JsonProperty("Source")
    private String Source;
    @JsonProperty("Number_of_Reads")
    private String NumberOfReads;
    @JsonProperty("Total_Number_of_Bases")
    private String TotalNumberOfBases;
    @JsonProperty("GC_Percentage")
    private String GCPercentage;
    @JsonProperty("Mean_Read_Length")
    private String MeanReadLength;
    @JsonProperty("Read_Length_Std_Dev")
    private String ReadLengthStdDev;
    @JsonProperty("Phred_Type")
    private String PhredType;
    @JsonProperty("Number_of_Duplicate_Reads")
    private String NumberOfDuplicateReads;
    @JsonProperty("Quality_Score_Min_Max")
    private String QualityScoreMinMax;
    @JsonProperty("Quality_Score_Mean_Std_Dev")
    private String QualityScoreMeanStdDev;
    @JsonProperty("Insert_Size_Mean")
    private String InsertSizeMean;
    @JsonProperty("Insert_Size_Std_Dev")
    private String InsertSizeStdDev;
    @JsonProperty("Outward_Read_Orientation")
    private String OutwardReadOrientation;
    @JsonProperty("Base_Percentages")
    private String BasePercentages;
    private Map<String, Object> additionalProperties = new HashMap<String, Object>();

    @JsonProperty("id")
    public String getId() {
        return id;
    }

    @JsonProperty("id")
    public void setId(String id) {
        this.id = id;
    }

    public ReadsInfoAll withId(String id) {
        this.id = id;
        return this;
    }

    @JsonProperty("Name")
    public String getName() {
        return Name;
    }

    @JsonProperty("Name")
    public void setName(String Name) {
        this.Name = Name;
    }

    public ReadsInfoAll withName(String Name) {
        this.Name = Name;
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

    public ReadsInfoAll withWorkspaceName(String workspaceName) {
        this.workspaceName = workspaceName;
        return this;
    }

    @JsonProperty("Type")
    public String getType() {
        return Type;
    }

    @JsonProperty("Type")
    public void setType(String Type) {
        this.Type = Type;
    }

    public ReadsInfoAll withType(String Type) {
        this.Type = Type;
        return this;
    }

    @JsonProperty("Platform")
    public String getPlatform() {
        return Platform;
    }

    @JsonProperty("Platform")
    public void setPlatform(String Platform) {
        this.Platform = Platform;
    }

    public ReadsInfoAll withPlatform(String Platform) {
        this.Platform = Platform;
        return this;
    }

    @JsonProperty("Single_Genome")
    public String getSingleGenome() {
        return SingleGenome;
    }

    @JsonProperty("Single_Genome")
    public void setSingleGenome(String SingleGenome) {
        this.SingleGenome = SingleGenome;
    }

    public ReadsInfoAll withSingleGenome(String SingleGenome) {
        this.SingleGenome = SingleGenome;
        return this;
    }

    @JsonProperty("Strain")
    public String getStrain() {
        return Strain;
    }

    @JsonProperty("Strain")
    public void setStrain(String Strain) {
        this.Strain = Strain;
    }

    public ReadsInfoAll withStrain(String Strain) {
        this.Strain = Strain;
        return this;
    }

    @JsonProperty("Source")
    public String getSource() {
        return Source;
    }

    @JsonProperty("Source")
    public void setSource(String Source) {
        this.Source = Source;
    }

    public ReadsInfoAll withSource(String Source) {
        this.Source = Source;
        return this;
    }

    @JsonProperty("Number_of_Reads")
    public String getNumberOfReads() {
        return NumberOfReads;
    }

    @JsonProperty("Number_of_Reads")
    public void setNumberOfReads(String NumberOfReads) {
        this.NumberOfReads = NumberOfReads;
    }

    public ReadsInfoAll withNumberOfReads(String NumberOfReads) {
        this.NumberOfReads = NumberOfReads;
        return this;
    }

    @JsonProperty("Total_Number_of_Bases")
    public String getTotalNumberOfBases() {
        return TotalNumberOfBases;
    }

    @JsonProperty("Total_Number_of_Bases")
    public void setTotalNumberOfBases(String TotalNumberOfBases) {
        this.TotalNumberOfBases = TotalNumberOfBases;
    }

    public ReadsInfoAll withTotalNumberOfBases(String TotalNumberOfBases) {
        this.TotalNumberOfBases = TotalNumberOfBases;
        return this;
    }

    @JsonProperty("GC_Percentage")
    public String getGCPercentage() {
        return GCPercentage;
    }

    @JsonProperty("GC_Percentage")
    public void setGCPercentage(String GCPercentage) {
        this.GCPercentage = GCPercentage;
    }

    public ReadsInfoAll withGCPercentage(String GCPercentage) {
        this.GCPercentage = GCPercentage;
        return this;
    }

    @JsonProperty("Mean_Read_Length")
    public String getMeanReadLength() {
        return MeanReadLength;
    }

    @JsonProperty("Mean_Read_Length")
    public void setMeanReadLength(String MeanReadLength) {
        this.MeanReadLength = MeanReadLength;
    }

    public ReadsInfoAll withMeanReadLength(String MeanReadLength) {
        this.MeanReadLength = MeanReadLength;
        return this;
    }

    @JsonProperty("Read_Length_Std_Dev")
    public String getReadLengthStdDev() {
        return ReadLengthStdDev;
    }

    @JsonProperty("Read_Length_Std_Dev")
    public void setReadLengthStdDev(String ReadLengthStdDev) {
        this.ReadLengthStdDev = ReadLengthStdDev;
    }

    public ReadsInfoAll withReadLengthStdDev(String ReadLengthStdDev) {
        this.ReadLengthStdDev = ReadLengthStdDev;
        return this;
    }

    @JsonProperty("Phred_Type")
    public String getPhredType() {
        return PhredType;
    }

    @JsonProperty("Phred_Type")
    public void setPhredType(String PhredType) {
        this.PhredType = PhredType;
    }

    public ReadsInfoAll withPhredType(String PhredType) {
        this.PhredType = PhredType;
        return this;
    }

    @JsonProperty("Number_of_Duplicate_Reads")
    public String getNumberOfDuplicateReads() {
        return NumberOfDuplicateReads;
    }

    @JsonProperty("Number_of_Duplicate_Reads")
    public void setNumberOfDuplicateReads(String NumberOfDuplicateReads) {
        this.NumberOfDuplicateReads = NumberOfDuplicateReads;
    }

    public ReadsInfoAll withNumberOfDuplicateReads(String NumberOfDuplicateReads) {
        this.NumberOfDuplicateReads = NumberOfDuplicateReads;
        return this;
    }

    @JsonProperty("Quality_Score_Min_Max")
    public String getQualityScoreMinMax() {
        return QualityScoreMinMax;
    }

    @JsonProperty("Quality_Score_Min_Max")
    public void setQualityScoreMinMax(String QualityScoreMinMax) {
        this.QualityScoreMinMax = QualityScoreMinMax;
    }

    public ReadsInfoAll withQualityScoreMinMax(String QualityScoreMinMax) {
        this.QualityScoreMinMax = QualityScoreMinMax;
        return this;
    }

    @JsonProperty("Quality_Score_Mean_Std_Dev")
    public String getQualityScoreMeanStdDev() {
        return QualityScoreMeanStdDev;
    }

    @JsonProperty("Quality_Score_Mean_Std_Dev")
    public void setQualityScoreMeanStdDev(String QualityScoreMeanStdDev) {
        this.QualityScoreMeanStdDev = QualityScoreMeanStdDev;
    }

    public ReadsInfoAll withQualityScoreMeanStdDev(String QualityScoreMeanStdDev) {
        this.QualityScoreMeanStdDev = QualityScoreMeanStdDev;
        return this;
    }

    @JsonProperty("Insert_Size_Mean")
    public String getInsertSizeMean() {
        return InsertSizeMean;
    }

    @JsonProperty("Insert_Size_Mean")
    public void setInsertSizeMean(String InsertSizeMean) {
        this.InsertSizeMean = InsertSizeMean;
    }

    public ReadsInfoAll withInsertSizeMean(String InsertSizeMean) {
        this.InsertSizeMean = InsertSizeMean;
        return this;
    }

    @JsonProperty("Insert_Size_Std_Dev")
    public String getInsertSizeStdDev() {
        return InsertSizeStdDev;
    }

    @JsonProperty("Insert_Size_Std_Dev")
    public void setInsertSizeStdDev(String InsertSizeStdDev) {
        this.InsertSizeStdDev = InsertSizeStdDev;
    }

    public ReadsInfoAll withInsertSizeStdDev(String InsertSizeStdDev) {
        this.InsertSizeStdDev = InsertSizeStdDev;
        return this;
    }

    @JsonProperty("Outward_Read_Orientation")
    public String getOutwardReadOrientation() {
        return OutwardReadOrientation;
    }

    @JsonProperty("Outward_Read_Orientation")
    public void setOutwardReadOrientation(String OutwardReadOrientation) {
        this.OutwardReadOrientation = OutwardReadOrientation;
    }

    public ReadsInfoAll withOutwardReadOrientation(String OutwardReadOrientation) {
        this.OutwardReadOrientation = OutwardReadOrientation;
        return this;
    }

    @JsonProperty("Base_Percentages")
    public String getBasePercentages() {
        return BasePercentages;
    }

    @JsonProperty("Base_Percentages")
    public void setBasePercentages(String BasePercentages) {
        this.BasePercentages = BasePercentages;
    }

    public ReadsInfoAll withBasePercentages(String BasePercentages) {
        this.BasePercentages = BasePercentages;
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
        return ((((((((((((((((((((((((((((((((((((((((((((("ReadsInfoAll"+" [id=")+ id)+", Name=")+ Name)+", workspaceName=")+ workspaceName)+", Type=")+ Type)+", Platform=")+ Platform)+", SingleGenome=")+ SingleGenome)+", Strain=")+ Strain)+", Source=")+ Source)+", NumberOfReads=")+ NumberOfReads)+", TotalNumberOfBases=")+ TotalNumberOfBases)+", GCPercentage=")+ GCPercentage)+", MeanReadLength=")+ MeanReadLength)+", ReadLengthStdDev=")+ ReadLengthStdDev)+", PhredType=")+ PhredType)+", NumberOfDuplicateReads=")+ NumberOfDuplicateReads)+", QualityScoreMinMax=")+ QualityScoreMinMax)+", QualityScoreMeanStdDev=")+ QualityScoreMeanStdDev)+", InsertSizeMean=")+ InsertSizeMean)+", InsertSizeStdDev=")+ InsertSizeStdDev)+", OutwardReadOrientation=")+ OutwardReadOrientation)+", BasePercentages=")+ BasePercentages)+", additionalProperties=")+ additionalProperties)+"]");
    }

}
