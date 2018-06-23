;;; Directory Local Variables
;;; For more information see (info "(emacs) Directory Variables")

((nil
  (eval when
        (not
         (fboundp 'check-problem))
        (load-file
         (expand-file-name "~/projects/personal/my-project-euler/elisp.el"))))
 (clojure-mode
  (inf-clojure-generic-cmd . "lumo -d")))

