взвешивание монеток на весах фемиды (деление пространства поиска на три части)
взвешиваем две одинаковые кучки и если равны, ищем в третьей.

(defun make-heap (coin-index coin-list)
  (cons coin-index coin-list))


(defun get-heap-coin-index (heap)
  (car heap))


(defun get-heap-coin-list (heap)
  (cdr heap))


(defun get-heap-size (heap)
  (length (get-heap-coin-list heap)))


(defun get-heap-weight (heap)
  (eval (cons '+ (get-heap-coin-list heap))))


(defun get-n-items (list n)
  (if (<= n 0)
      '()
    (cons (car list) 
	  (get-n-items (cdr list) 
		       (- n 1)))))


(defun get-subheap-size (heap)
  (/ (+ (get-heap-size heap) 2) 3))


(defun make-subheap-1 (heap)
  (let ((subheap-size (get-subheap-size heap)))
    (make-heap (get-heap-coin-index heap)
	       (get-n-items (get-heap-coin-list heap)
			    subheap-size))))


(defun make-subheap-2 (heap)
  (let ((subheap-size (get-subheap-size heap)))
    (make-heap (+ (get-heap-coin-index heap) subheap-size)
	       (get-n-items (nthcdr subheap-size (get-heap-coin-list heap))
			    subheap-size))))


(defun make-subheap-3 (heap)
  (let ((subheap-size (get-subheap-size heap)))
    (make-heap (+ (get-heap-coin-index heap) (* subheap-size 2))
	       (nthcdr (* subheap-size 2) (get-heap-coin-list heap)))))


(defun search-heavy-coin (heap)
  (cond ((>= 1 (get-heap-size heap)) (get-heap-coin-index heap))
	(t (let ((subheap-1 (make-subheap-1 heap))
		 (subheap-2 (make-subheap-2 heap))
		 (subheap-3 (make-subheap-3 heap)))

	     (cond ((> (get-heap-weight subheap-1) 
		       (get-heap-weight subheap-2)) (search-heavy-coin subheap-1))
		   ((< (get-heap-weight subheap-1) 
		       (get-heap-weight subheap-2)) (search-heavy-coin subheap-2))
		   (t (search-heavy-coin subheap-3)))))))


(defun search-heavy-coin-in-list (list)
  (search-heavy-coin (make-heap 0 list)))


(let ((coins '(1 1 1 1 5 1)))
  (progn (princ "Coin index is ")
	 (princ (search-heavy-coin-in-list coins))
	 (princ ", Coin weight is ")
	 (princ (nth (search-heavy-coin-in-list coins) coins))
	 (princ ".")
	 (terpri)))


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

