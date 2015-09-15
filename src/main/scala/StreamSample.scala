import org.apache.spark.{SparkContext, SparkConf}
import org.apache.spark.streaming.StreamingContext
import org.apache.spark.streaming.StreamingContext._
import org.apache.spark.streaming.dstream.DStream
import org.apache.spark.streaming.Duration
import org.apache.spark.streaming.Seconds

object StreamSample {
  def main(args: Array[String]) :Unit = {

    val conf = new SparkConf().setAppName("WordCount Application")
    conf.setMaster("local[*]")


    val ssc = new StreamingContext(conf,Seconds(5))
    val lines = ssc.socketTextStream("localhost",12001)

    val text =lines.filter(_.contains("but"))
    text.print()

    ssc.start()
    ssc.awaitTermination()
  }
}