import java.util.Scanner;
import java.io.IOException;

public class util {

    static Scanner kb = new Scanner(System.in);

    /**
     * Force the user to input a valid integer in a range of two integers
     * 
     * @param msg The message we want to print
     * @param min The minimum value accepted
     * @param max The maximum value accepted
     * @return The valid integer
     */
    public static int askIntRange(String msg, int min, int max) {
        fastPrint("" + msg + " (" + min + "/" + max + ") : ");
        while (!kb.hasNextInt()) {
            fastPrint("! Please enter a valid number : ");
            kb.next();
        }
        int result = kb.nextInt();
        kb.nextLine(); /* Delete '\n' char in 'kb' buffer */
        while (result < min || result > max) {
            fastPrint("! Please enter a number between " + min + " and " + max + " : ");
            while (!kb.hasNextInt()) {
                fastPrint("! Please enter a valid number : ");
                kb.next();
            }
            result = kb.nextInt();
            kb.nextLine(); /* Delete '\n' char in 'kb' buffer */
        }
        return result;
    }

    /**
     * Choose a random integer in a range of two integers
     * 
     * @param min The minimum value of the random integer
     * @param max The maximum value of the random integer
     * @return The random integer between min and max
     */
    public static int randomIntRange(int min, int max) {
        return (int) (min + Math.random() * (max - min + 1));
    }

    /**
     * Check if a variable is an integer or not
     * 
     * @param item The variable we want to check
     * @return True or False if the variable is a valid integer or not
     */
    public static boolean isInt(String item) {
        try {
            Integer.parseInt(item);
            return true;
        } catch (NumberFormatException ex) {
            return false;
        }
    }

    /**
     * Print a message and wait for the user to press 'Enter'
     */
    public static void enter() {
        fastPrint("Press enter to continue...");
        try {
            System.in.read();
        } catch (Exception ex) {
            fastPrint("! Unexpected 'read' error");
            sleep(1);
        }
    }

    /**
     * Lovely way to print a message like a typewriter The method waits 10 ms after
     * printing each char of the msg
     * 
     * @param msg The message we want to print
     */
    public static void fastPrint(String msg) {
        for (int i = 0; i < msg.length(); i++) {
            if (msg.charAt(i) == '\n') {
                System.out.println();
            } else {
                System.out.print(msg.charAt(i));
                sleep(0.01);
            }
        }
    }

    /**
     * Lovely way to print a message like a typewriter The method waits 100 ms after
     * printing each char of the msg Then waits 1 sec after the entire msg
     * 
     * @param msg
     */
    public static void slowPrint(String msg) {
        for (int i = 0; i < msg.length(); i++) {
            if (msg.charAt(i) == '\n') {
                System.out.println();
            } else {
                System.out.print(msg.charAt(i));
                sleep(0.1);
            }
        }
        sleep(1);
    }

    /**
     * The program waits a certain number of milliseconds before continuing
     * 
     * @param s The number of milliseconds
     */
    public static void sleep(double s) {
        int ms = (int) (s * 1000);
        try {
            Thread.sleep(ms);
        } catch (InterruptedException ex) {
            fastPrint("! <error> ('sleep' method)");
            Thread.currentThread().interrupt();
        }
    }

    /**
     * Clear the screen of the user (I'm sure this works on Windows, and I hope this
     * will work on Linux and MacOs too... I'm praying !)
     */
    public static void clearScreen() {
        String os = System.getProperty("os.name");
        try {
            if (os.contains("Windows")) {
                new ProcessBuilder("cmd", "/c", "cls").inheritIO().start().waitFor();
            } else {
                System.out.print("\033\143");
            }
        } catch (IOException | InterruptedException ex) {
            System.out.println("! <error> ('clearScreen' method)");
            sleep(1);
        }
    }

    public static boolean fileExists(String path) {
        File file = new File(path);
        if (file.exists() && !file.isDirectory()) {
            return true;
        }
        return false;
    }

    public static String[] getFiles() {
        String[] allPaths;
        File file = new File(".");
        allPaths = file.list();
        int cpt = 0;
        for (String path : allPaths) {
            if (path.endsWith(".txt") && !path.equals("Save.txt")) {
                cpt++;
            }
        }
        if (cpt == 0) {
            String[] txtFiles = { "<error> No txt files found" };
            return txtFiles;
        } else {
            String[] txtFiles = new String[cpt];
            cpt = 0;
            for (String path : allPaths) {
                if (path.endsWith(".txt") && !path.equals("Save.txt")) {
                    txtFiles[cpt] = path;
                    cpt++;
                }
            }
            return txtFiles;
        }
    }

    public static String saveFile(String mode, String path, String[] text) {
        String newPath = "";
        for (int i = 0; i < path.length() - 4; i++) {
            newPath += path.charAt(i);
        }
        if (mode.equals("CRYPTED")) {
            newPath += "-crypted.txt";
        } else {
            newPath += "-decrypted.txt";
        }
        try {
            File file = new File(newPath);
            file.createNewFile();
        } catch (IOException ex) {
            System.out.println("\n\n! <error> Couldn't open file [Save.txt] ('saveFile' method)");
        }
        try {
            FileWriter file = new FileWriter(newPath, StandardCharsets.UTF_8);
            for (int i = 0; i < text.length; i++) {
                file.write(text[i]);
                if (i < text.length - 1) {
                    file.write("\n");
                }
            }
            file.close();
        } catch (IOException e) {
            System.out.println("\n\n! <error> Couldn't write in file [Save.txt] ('saveFile' method)");
            e.printStackTrace();
        }
        return newPath;
    }

    public static String[] readFile(String path, String[] text, int nbLines) {
        File file = new File(path);
        try {
            FileReader fileReader = new FileReader(file, StandardCharsets.UTF_8);
            BufferedReader br = new BufferedReader(fileReader);
            String line;
            int cpt = 0;
            while ((line = br.readLine()) != null) {
                text[cpt] = line;
                cpt++;
            }
            br.close();
            fileReader.close();
        } catch (FileNotFoundException ex) {
            System.out.println("! <error> File [" + path + "] doesn't exist ('readFile' method)");
        } catch (IOException ex) {
            ex.printStackTrace();
        }
        return text;
    }

    public static int fileLineCounter(String path) {
        int cpt = 0;
        try {
            Scanner input = new Scanner(new File(path));
            while (input.hasNextLine()) {
                String useless = input.nextLine();
                cpt++;
            }
        } catch (FileNotFoundException ex) {
            System.out.println("! <error> File [" + path + "] doesn't exist ('readFile' method)");
        }
        return cpt;
    }

    public static String askValidFileName(String mode, String[] files) {
        String path = "";
        if (System.console() == null) {
            util.fastPrint("Which file do you want to " + mode + " ? : ");
            path = kb.nextLine();
            while (path.equals("")) {
                util.fastPrint("! Please write something : ");
                path = kb.nextLine();
            }
            while (isInt(path)) {
                if (Integer.parseInt(path) == 0) {
                    path = "0.txt";
                } else if (Integer.parseInt(path) > 0 && Integer.parseInt(path) <= files.length) {
                    path = files[Integer.parseInt(path) - 1];
                } else {
                    util.fastPrint("! Please enter a number between 0 and " + files.length + " : ");
                    path = kb.nextLine();
                }
            }
            if (!path.endsWith(".txt")) {
                path += ".txt";
            }
            while (!util.fileExists(path) && !path.equals("0.txt") && !path.equals("exit.txt")
                    && !path.equals("quit.txt")) {
                util.fastPrint("File [" + path + "] doesn't exist here, try again : ");
                path = kb.nextLine();
                while (path.equals("")) {
                    util.fastPrint("! Please write something : ");
                    path = kb.nextLine();
                }
                while (isInt(path)) {
                    if (Integer.parseInt(path) == 0) {
                        path = "0.txt";
                    } else if (Integer.parseInt(path) > 0 && Integer.parseInt(path) <= files.length) {
                        path = files[Integer.parseInt(path) - 1];
                    } else {
                        util.fastPrint("! Please enter a number between 0 and " + files.length + " : ");
                        path = kb.nextLine();
                    }
                }
                if (!path.endsWith(".txt")) {
                    path += ".txt";
                }
            }
            while (!path.equals("0.txt") && !path.equals("exit.txt") && !path.equals("quit.txt")
                    && fileLineCounter(path) <= 0) {
                util.fastPrint("File [" + path + "] is empty, try another one : ");
                path = kb.nextLine();
                while (isInt(path)) {
                    if (Integer.parseInt(path) == 0) {
                        path = "0.txt";
                    } else if (Integer.parseInt(path) > 0 && Integer.parseInt(path) <= files.length) {
                        path = files[Integer.parseInt(path) - 1];
                    } else {
                        util.fastPrint("! Please enter a number between 0 and " + files.length + " : ");
                        path = kb.nextLine();
                    }
                }
                if (!path.endsWith(".txt")) {
                    path += ".txt";
                }
                while (!util.fileExists(path) && !path.equals("0.txt") && !path.equals("exit.txt")
                        && !path.equals("quit.txt")) {
                    util.fastPrint("File [" + path + "] doesn't exist here, try again : ");
                    path = kb.nextLine();
                    while (path.equals("")) {
                        util.fastPrint("! Please write something : ");
                        path = kb.nextLine();
                    }
                    while (isInt(path)) {
                        if (Integer.parseInt(path) == 0) {
                            path = "0.txt";
                        } else if (Integer.parseInt(path) > 0 && Integer.parseInt(path) <= files.length) {
                            path = files[Integer.parseInt(path) - 1];
                        } else {
                            util.fastPrint("! Please enter a number between 0 and " + files.length + " : ");
                            path = kb.nextLine();
                        }
                    }
                    if (!path.endsWith(".txt")) {
                        path += ".txt";
                    }
                }
            }
        } else {
            util.fastPrint("Which file do you want to " + mode + " ? : ");
            path = System.console().readLine();
            while (path.equals("")) {
                util.fastPrint("! Please write something : ");
                path = System.console().readLine();
            }
            while (isInt(path)) {
                if (Integer.parseInt(path) == 0) {
                    path = "0.txt";
                } else if (Integer.parseInt(path) > 0 && Integer.parseInt(path) <= files.length) {
                    path = files[Integer.parseInt(path) - 1];
                } else {
                    util.fastPrint("! Please enter a number between 0 and " + files.length + " : ");
                    path = System.console().readLine();
                }
            }
            if (!path.endsWith(".txt")) {
                path += ".txt";
            }
            while (!util.fileExists(path) && !path.equals("0.txt") && !path.equals("exit.txt")
                    && !path.equals("quit.txt")) {
                util.fastPrint("File [" + path + "] doesn't exist here, try again : ");
                path = System.console().readLine();
                while (path.equals("")) {
                    util.fastPrint("! Please write something : ");
                    path = System.console().readLine();
                }
                while (isInt(path)) {
                    if (Integer.parseInt(path) == 0) {
                        path = "0.txt";
                    } else if (Integer.parseInt(path) > 0 && Integer.parseInt(path) <= files.length) {
                        path = files[Integer.parseInt(path) - 1];
                    } else {
                        util.fastPrint("! Please enter a number between 0 and " + files.length + " : ");
                        path = System.console().readLine();
                    }
                }
                if (!path.endsWith(".txt")) {
                    path += ".txt";
                }
            }
            while (!path.equals("0.txt") && !path.equals("exit.txt") && !path.equals("quit.txt")
                    && fileLineCounter(path) <= 0) {
                util.fastPrint("File [" + path + "] is empty, try another one : ");
                path = System.console().readLine();
                while (isInt(path)) {
                    if (Integer.parseInt(path) == 0) {
                        path = "0.txt";
                    } else if (Integer.parseInt(path) > 0 && Integer.parseInt(path) <= files.length) {
                        path = files[Integer.parseInt(path) - 1];
                    } else {
                        util.fastPrint("! Please enter a number between 0 and " + files.length + " : ");
                        path = System.console().readLine();
                    }
                }
                if (!path.endsWith(".txt")) {
                    path += ".txt";
                }
                while (!util.fileExists(path) && !path.equals("0.txt") && !path.equals("exit.txt")
                        && !path.equals("quit.txt")) {
                    util.fastPrint("File [" + path + "] doesn't exist here, try again : ");
                    path = System.console().readLine();
                    while (path.equals("")) {
                        util.fastPrint("! Please write something : ");
                        path = System.console().readLine();
                    }
                    while (isInt(path)) {
                        if (Integer.parseInt(path) == 0) {
                            path = "0.txt";
                        } else if (Integer.parseInt(path) > 0 && Integer.parseInt(path) <= files.length) {
                            path = files[Integer.parseInt(path) - 1];
                        } else {
                            util.fastPrint("! Please enter a number between 0 and " + files.length + " : ");
                            path = System.console().readLine();
                        }
                    }
                    if (!path.endsWith(".txt")) {
                        path += ".txt";
                    }
                }
            }
        }
        return path;
    }

    public static String askValidMsg(String mode) {
        String msg = "";
        if (System.console() == null) {
            util.fastPrint("Please write the sentence you want to " + mode + " : ");
            msg = kb.nextLine();
            while (msg.equals("")) {
                util.fastPrint("! Please write something : ");
                msg = kb.nextLine();
            }
            while (!checkASCII(msg)) {
                fastPrint("! Please write a valid sentence : ");
                msg = System.console().readLine();
                while (msg.equals("")) {
                    fastPrint("! Please write something : ");
                    msg = System.console().readLine();
                }
            }
        } else {
            util.fastPrint("Please write the sentence you want to " + mode + " : ");
            msg = System.console().readLine();
            while (msg.equals("")) {
                util.fastPrint("! Please write something : ");
                msg = System.console().readLine();
            }
        }
        return msg;
    }

    public static String askValidKey() {
        String key = "";
        if (System.console() == null) {
            fastPrint("Please enter the key : ");
            key = kb.nextLine();
            while (key.equals("")) {
                fastPrint("! Please write something : ");
                key = kb.nextLine();
            }
            while (!checkASCII(key)) {
                fastPrint("! Please enter a valid key : ");
                key = kb.nextLine();
                while (key.equals("")) {
                    fastPrint("! Please write something : ");
                    key = kb.nextLine();
                }
            }
        } else {
            fastPrint("Please enter the key : ");
            key = System.console().readLine();
            while (key.equals("")) {
                fastPrint("! Please write something : ");
                key = System.console().readLine();
            }
            while (!checkASCII(key)) {
                fastPrint("! Please enter a valid key : ");
                key = System.console().readLine();
                while (key.equals("")) {
                    fastPrint("! Please write something : ");
                    key = System.console().readLine();
                }
            }
        }
        return key;
    }

    public static boolean checkASCII(String msg) {
        String test = "";
        for (int i = 0; i < msg.length(); i++) {
            if ((int) msg.charAt(i) < 32 || (int) msg.charAt(i) > 126) {
                fastPrint("! <error> [" + test + "] next character [" + msg.charAt(i) + "] forbidden (ASCII="
                        + (int) msg.charAt(i) + ")\n");
                return false;
            }
            test = test + msg.charAt(i);
        }
        return true;
    }
}