class Node {
public:
    Node next;
    Node previous;
    int data;

    Node(int data) {
        this.data = data;
    }

    void append(int data) {
        Node end = Node(data);
        Node n = this;
        while(n.next != NULL) {
            n = n.next;
        }

        n.next = end;
    }
};
