import lombok.Data;
import lombok.EqualsAndHashCode;
import io.swagger.annotations.ApiModelProperty;
import cn.bensun.api.thirdParty.domain.BaseEntity;
/**
 * @Classname ${className}
 * @Description TODO
 * @Date ${time}
 * @Created by weizongtang
 */
@EqualsAndHashCode(callSuper = true)
@Data
public class ${className}  extends BaseEntity{
    <columnName>
    @ApiModelProperty(value = "${remark}")
    private String ${columnName};
    </columnName>
}
