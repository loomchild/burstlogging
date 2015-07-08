import ch.qos.logback.core.Appender;
import ch.qos.logback.core.AppenderBase;

public class BurstAppender<E> extends AppenderBase<E> {

    private Appender<E> target;

    public BurstAppender(Appender<E> target) {
        this.target = target;
    }

    @Override
    protected void append(E eventObject) {

    }

}
