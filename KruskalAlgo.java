import java.util.ArrayList;
import java.util.Collections;
import java.util.Comparator;

class Edge {
    int src, dest, weight;

    Edge(int src, int dest, int weight) {
        this.src = src;
        this.dest = dest;
        this.weight = weight;
    }

    public String toString() {
        return "(" + src + ", " + dest + ", " + weight + ")";
    }
}

class MySorter implements Comparator<Edge>{
    public int compare(Edge a, Edge b){
        return a.src - b.src;
    }
}

class EdgeSorter implements Comparator<Edge> {
    public int compare(Edge a, Edge b) {
        return a.weight - b.weight;
    }
}

public class KruskalAlgo {

    public static boolean isThere(ArrayList<Edge> myal, Edge a) {
        for (int k = 0; k < myal.size(); k++) {
            if (myal.get(k) == a) {
                return true;
            }
        }
        return false;
    }

    public static ArrayList<Edge> mst(ArrayList<ArrayList<Edge>> graph) {

        for (int i = 0; i < graph.size(); i++) {
            Collections.sort(graph.get(i), new EdgeSorter());
        }

        ArrayList<Edge> myal = new ArrayList<>();
        for (int i = 0; i < graph.size(); i++) {
            for (int j = 0; j < graph.size(); j++) {
                Edge a = graph.get(i).get(0);
                Edge b = graph.get(j).get(0);
                if (b.weight < a.weight && a != b) {
                    if (!isThere(myal, b)) {
                        myal.add(b);
                        graph.get(j).remove(b);

                        if (graph.get(j).isEmpty()) {
                            graph.remove(j);
                        }
                    }
                    if (i >= graph.size()) {
                        return myal;
                    }
                }
            }
        }
        return myal;
    }

    public static void main(String[] args) {
        ArrayList<ArrayList<Edge>> graph = new ArrayList<ArrayList<Edge>>(3);
        ArrayList<Edge> al = new ArrayList<>();
        ArrayList<Edge> bl = new ArrayList<>();
        ArrayList<Edge> cl = new ArrayList<>();
        ArrayList<Edge> dl = new ArrayList<>();
        al.add(new Edge(1, 2, 2));
        al.add(new Edge(1, 3, 5));
        bl.add(new Edge(2, 3, 6));
        bl.add(new Edge(2, 4, 7));
        bl.add(new Edge(2, 5, 1));
        cl.add(new Edge(3, 5, 9));
        dl.add(new Edge(4, 5, 3));
        graph.add(al);
        graph.add(bl);
        graph.add(cl);
        graph.add(dl);
        ArrayList<ArrayList<Edge>> tempGraph = new ArrayList<>();
        for (int i = 0; i < graph.size(); i++) {
            tempGraph.add((ArrayList<Edge>)graph.get(i).clone());
        }
        ArrayList<Edge> minSpanTree = mst(tempGraph);
        Collections.sort(minSpanTree, new MySorter());
        System.out.println(minSpanTree);
    }
}