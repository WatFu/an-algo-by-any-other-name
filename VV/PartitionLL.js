// I: head of LL, x integer
// O: head of new LL
// C: null
// E: LL of len(0, 1), x greater than or less than all nodes

//
// p = listNode(0);

// q = listNode(0);
// head = ListNode starting
// while head !== null:
//      if (head.val >= x):
//      p.next = head
//      p = p.next

sortLinkedLIst = (head, x) => {
  if (!head) {
    return null;
  }
  let p = ListNode(0);
  const phead = p;
  let q = ListNode(0);
  const qhead = q;

  while (head) {
    if (head.val > x) {
      p.next = head;
      p = p.next;
    } else {
      q.next = head;
      q = q.next;
    }
    head = head.next;
  }
  p.next = null;
  q.next = phead.next;
  return qhead.next
}


reverseLinkedLst = (head) => {
  p = head;
  q = head.next;
  p.next = null;

  while (q) {
    tmp = q.next;
    q.next = p;
    p = q;
    q = tmp;
  }
  return p
}