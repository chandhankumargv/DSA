class MyQueue {
     Stack<Integer> inbox = new Stack<>();
     Stack<Integer> outbox = new Stack<>();

    public MyQueue() {
      

    }
    
    public void push(int x) {
        inbox.push(x);
    }
    
    public int pop() {
        if(outbox.isEmpty()){
            while(!inbox.isEmpty()){
                outbox.push(inbox.pop());
            }
        }
        return outbox.pop();
        
    }
    
    public int peek() {
        if(outbox.isEmpty()){
            while(!inbox.isEmpty()){
                outbox.push(inbox.pop());
            }
        }
        return outbox.peek();
    }
    
    public boolean empty() {
        return inbox.isEmpty() && outbox.isEmpty();
    }
}

/**
 * Your MyQueue object will be instantiated and called as such:
 * MyQueue obj = new MyQueue();
 * obj.push(x);
 * int param_2 = obj.pop();
 * int param_3 = obj.peek();
 * boolean param_4 = obj.empty();
 */