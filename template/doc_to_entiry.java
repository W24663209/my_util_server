import lombok.Data;
import lombok.EqualsAndHashCode;
import cn.bensun.common.annotation.TableFieldComment;
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
    @TableFieldComment(value = "${remark}")
    private String ${columnName};
    </columnName>
}
