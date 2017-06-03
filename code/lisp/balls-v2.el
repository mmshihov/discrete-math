взвешивание монеток на весах фемиды (деление пространства поиска на три части)
взвешиваем две одинаковые кучки и если равны, ищем в третьей.



(defun search-heavy-coin-in-list (coins)
  
  (defun make-heap (coin-index coin-list)
    (cons coin-index coin-list))

  (defun search-heavy-coin (heap)

    (defun get-heap-coin-index (heap)
      (car heap))


    (defun get-heap-coin-list (heap)
      (cdr heap))


    (defun get-heap-weight (heap)
      (eval (cons '+ (get-heap-coin-list heap))))


    (defun get-n-items (list n)
      (if (or (null list) (<= n 0))
	  '()
	(cons (car list) 
	      (get-n-items (cdr list) 
			   (- n 1)))))


    (defconst heap-size (length (get-heap-coin-list heap)))


    (defconst subheap-size
      (/ (+ heap-size 2) 3))


    (defconst subheap-1
      (make-heap (get-heap-coin-index heap)
		 (get-n-items (get-heap-coin-list heap)
			      subheap-size)))


    (defconst subheap-2
      (make-heap (+ (get-heap-coin-index heap) subheap-size)
		 (get-n-items (nthcdr subheap-size (get-heap-coin-list heap))
			      subheap-size)))
  

    (defconst subheap-3 
      (make-heap (+ (get-heap-coin-index heap) (* subheap-size 2))
		 (nthcdr (* subheap-size 2) (get-heap-coin-list heap))))


    (cond ((>= 1 heap-size) (get-heap-coin-index heap))
	  (t (cond ((> (get-heap-weight subheap-1) 
		       (get-heap-weight subheap-2)) (search-heavy-coin subheap-1))
		   ((< (get-heap-weight subheap-1) 
		       (get-heap-weight subheap-2)) (search-heavy-coin subheap-2))
		   (t (search-heavy-coin subheap-3))))))

  (search-heavy-coin (make-heap 0 coins)))


(let ((coins '(1 1 1 1 5 1)))
  (progn (princ "Coin index is ")
	 (princ (search-heavy-coin-in-list coins))
	 (princ ", Coin weight is ")
	 (princ (nth (search-heavy-coin-in-list coins) coins))
	 (princ ".")
	 (terpri)))
Coin index is 4, Coin weight is 5.
t

Coin index is 
Coin index is 
Coin index is 
Coin index is 

Coin index is 
Coin index is 
Coin index is 


тесты:
(make-heap 0 '(1 1 1 1 2))
(get-heap-coin-index (make-heap 0 '(1 1 1 1 2)))
(get-heap-coin-list (make-heap 0 '(1 1 1 1 2)))
(get-heap-size (make-heap 0 '(1)))
(get-heap-weight (make-heap 0 '(1 1 1 2)))
(get-heap-weight (make-heap 0 '(1)))
(get-heap-weight (make-heap 0 '()))
(get-n-items '(0) 3)
(get-n-items '(0 1 2 3) 3)
(get-subheap-size (make-heap 0 '(1 1 1)))
(let ((heap (make-heap 0 '(1 ))))
  (make-subheap-1 heap))
(let ((heap (make-heap 3 '(1 2 3 4 5 6 7))))
  (make-subheap-2 heap))
(let ((heap (make-heap 0 '(1 2 3 4 5 6 7 8 9 10))))
  (make-subheap-3 heap))
(search-heavy-coin (make-heap 0 '(1 1 1 2 1)))


проверки:
(nthcdr -2 '(0 1 2 3 4))
=>(2 3 4)
(append (list 2 3 4) 1)
=>(2 3 4 . 1)

(defun foo (x)

  (defconst bar (+ x x))

  (cond
   ((= x 0) 1)
   (t (progn 
	(princ "x")
	(princ x)
	(princ "bar(x)")
	(princ bar)
	(terpri)
	(foo (- x 1))))))
foo



(foo 3)
x3bar(x)6
x2bar(x)4
x1bar(x)2
1

x3bar(x)6
x2bar(x)6
x1bar(x)6
1

x3bar(x)
x3bar(x)6
x2bar(x)4
x1bar(x)2
1



